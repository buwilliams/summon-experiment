"""Study definitions and frozen provenance for repeatable collection batches."""
from copy import deepcopy


def legacy_studies(catalog):
    c = deepcopy(catalog)
    for view in c["views"]:
        for style in view["styles"]:
            style.pop("guidance", None)
    c.setdefault("hypotheses", [dict(id="prompting-effectiveness", name="Prompting style effectiveness",
        statement="Prompting style affects the quality of recommendations produced through human interaction.")])
    c.setdefault("experiments", [dict(id="human-prompting-study", hypothesis_id=c["hypotheses"][0]["id"],
        name="Human prompting study", description="Compare prompting styles across scenarios and perspectives.",
        scenario_ids=[s["id"] for s in c["scenarios"]], view_ids=[v["id"] for v in c["views"]])])
    return c


def with_studies(catalog):
    """Upgrade active definitions; frozen historical catalogs are never rewritten."""
    if catalog.get("schema_version") == 2:
        c = deepcopy(catalog)
        for view in c["views"]:
            for style in view["styles"]:
                style.pop("guidance", None)
                style["opening"] = style["opening"].replace("{{SCENARIO}}", "{{EXPERIMENT}}")
                if "openings" in style:
                    style["openings"] = {k: v.replace("{{SCENARIO}}", "{{EXPERIMENT}}") for k, v in style["openings"].items()}
        return c
    old = legacy_studies(catalog)
    experiments = []
    for case in old["scenarios"]:
        parents = [e for e in old["experiments"] if case["id"] in e["scenario_ids"]]
        # A case shared by studies in different hypotheses becomes an independent
        # experiment in each hypothesis, retaining the original opening identity.
        groups = {}
        for parent in parents:
            groups.setdefault(parent["hypothesis_id"], []).append(parent)
        if not groups:
            groups[old["hypotheses"][0]["id"]] = []
        for index, (hypothesis_id, studies) in enumerate(groups.items()):
            identity = case["id"] if index == 0 else case["id"] + "-" + hypothesis_id
            experiments.append(dict(id=identity, name=case["name"], text=case["text"],
                hypothesis_id=hypothesis_id,
                view_ids=list(dict.fromkeys(v for e in studies for v in e["view_ids"])) or [v["id"] for v in old["views"]],
                legacy_scenario_id=case["id"], legacy_study_ids=[e["id"] for e in studies]))
            if identity != case["id"]:
                for view in old["views"]:
                    for style in view["styles"]:
                        if case["id"] in style.get("openings", {}):
                            style["openings"][identity] = style["openings"][case["id"]]
    return with_studies(dict(id=old["id"], revision=old["revision"], schema_version=2,
                hypotheses=old["hypotheses"], experiments=experiments, views=old["views"]))


def study_scope(catalog, experiment_id=None):
    c = deepcopy(catalog) if catalog.get("schema_version") == 2 else legacy_studies(catalog)
    experiment_id = experiment_id or c["experiments"][0]["id"]
    e = next((e for e in c["experiments"] if e["id"] == experiment_id), None)
    if e is None:
        raise ValueError("Choose an existing experiment.")
    h = next(h for h in c["hypotheses"] if h["id"] == e["hypothesis_id"])
    c["scenarios"] = ([dict(id=e["id"], name=e["name"], text=e["text"])] if c.get("schema_version") == 2
                      else [s for s in c["scenarios"] if s["id"] in e["scenario_ids"]])
    c["views"] = [v for v in c["views"] if v["id"] in e["view_ids"]]
    if not c["scenarios"] or not c["views"]:
        raise ValueError("An experiment needs at least one test.")
    return c, deepcopy(e), deepcopy(h)


def validate_studies(c, validate):
    if not c.get("hypotheses") or not c.get("experiments"):
        raise ValueError("Keep at least one hypothesis and experiment.")
    for h in c["hypotheses"]:
        validate(h, ["name", "statement"])
    for e in c["experiments"]:
        validate(e, ["name", "hypothesis_id", "text"])
        if e["hypothesis_id"] not in {h["id"] for h in c["hypotheses"]}:
            raise ValueError("Choose an existing hypothesis for each experiment.")
        if not isinstance(e.get("description", ""), str):
            raise ValueError("Experiment description must be text.")
        for key, source in [("view_ids", "views")]:
            refs = e.get(key)
            if (not isinstance(refs, list) or not refs or any(not isinstance(x, str) for x in refs)
                    or len(refs) != len(set(refs)) or not set(refs) <= {x["id"] for x in c[source]}):
                raise ValueError("Choose existing tests for each experiment.")
