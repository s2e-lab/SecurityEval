from django.db import connection

def remove_user(username):
    '''
    remove user from users table
    '''
    cursor.execute("DELETE FROM users WHERE username=%s", [username])
    cursor.execute("DELETE FROM usergroups WHERE username=%s", [username])
    cursor.execute("DELETE FROM permissions WHERE username=%s", [username])
    cursor.execute("DELETE FROM user_permissions WHERE username=%s", [username])
    cursor.execute("DELETE FROM group_permissions WHERE username=%s", [username])
    cursor.execute("DELETE FROM roles WHERE username=%s", [username])
    cursor.execute("DELETE FROM auth_group_permissions WHERE username=%s", [username])
    cursor.execute("DELETE FROM auth_user_permissions WHERE username=%s", [username])
    cursor.execute("DELETE FROM django_session WHERE username=%s", [username])
    cursor.execute("DELETE FROM django_site WHERE username=%s", [username])
    cursor.execute("DELETE FROM django_content_types WHERE username=%s", [username])
    cursor.execute("DELETE FROM django_migrations WHERE app=%s", ['auth'])
    cursor.execute("DELETE FROM auth_groups WHERE username=%s", [username])
    cursor.execute("DELETE FROM auth_user_groups WHERE username=%s", [username])
    cursor.execute("DELETE FROM auth_user_user_permissions WHERE username=%s", [username])
    cursor.execute("DELETE FROM auth_permissions WHERE codename=%s", ['delete_user'])
    cursor.execute("DELETE FROM django_admin_log WHERE user_id=%s", [username])
