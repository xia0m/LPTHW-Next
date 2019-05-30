class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    else:
        for g in group.get_groups():
            if is_user_in_group(user, g):
                return True
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

# Test Case 1 None input
sub_child_user_none = None
sub_child.add_user(sub_child_user_none)
print(f"None input: {is_user_in_group(sub_child_user_none, sub_child)}")
# expected: True

# Test Case 2 Empty Input

sub_child_user_empty = ""
sub_child.add_user(sub_child_user_empty)
print(f"Empty input: {is_user_in_group(sub_child_user_empty, sub_child)}")
# expected: True

# Test Case 3

sub_child_user = "sub_child_user"
sub_child_user2 = 'sub_child_user2'
sub_child.add_user(sub_child_user)
sub_child.add_user(sub_child_user2)


child_user = 'child_user'
child.add_user(child_user)

child.add_group(sub_child)
parent.add_group(child)

print(
    f"Sub child user is in sub child: {is_user_in_group(sub_child_user, sub_child)}")
# expected: True
print(
    f"Sub child user is in child: {is_user_in_group(sub_child_user, child)}")
# expected: True
print(
    f"Sub child user is in parent: {is_user_in_group(sub_child_user, parent)}")
# expected: True
print(
    f"Child user is not in sub child: {is_user_in_group(child_user, sub_child)}")
# expected: False

print(
    f"random input is not in any group: {is_user_in_group('test', sub_child)}")
# exptected: False
print(
    f"random input is not in any group: {is_user_in_group('test', child)}")
# expected: False
print(
    f"random input is not in any group: {is_user_in_group('test', parent)}")
# expected: False
