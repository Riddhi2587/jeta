from maml import maml_adapt

def test_maml_adapt():
    theta = params["params"]
    theta_new = maml_adapt(params, apply_fn, loss_fn, support_set)
    assert theta != theta_new