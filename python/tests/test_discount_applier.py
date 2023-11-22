from discount_applier import DiscountApplier

def test_apply_v1():

    notified_users =[]
    class Notifier:
        def notify(self, user, message):
            notified_users.append(user)

    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v1
    n = Notifier()
    da = DiscountApplier(n)
    users = ['Nico']

    da.apply_v1(10, users)

    assert len(notified_users) == 1
    pass


def test_apply_v2():
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v2
    
    
    pass
