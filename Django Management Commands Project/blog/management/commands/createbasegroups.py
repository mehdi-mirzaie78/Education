from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Post


class Command(BaseCommand):
    help = """
    Creates these groups:
    Editor => View & Change & Delete
    Viewer => View
    Author => Add & View 
    """

    names = ['editor', 'viewer', 'author']

    def add_arguments(self, parser):
        parser.add_argument("names", nargs="*", type=str, default=self.names, help="Names of groups")
        parser.add_argument("-d", "--delete", action="store_true")

    def handle(self, *args, **kwargs):
        group_names = kwargs["names"]
        if kwargs["delete"]:
            queryset = Group.objects.filter(name__in=group_names)
            queryset.delete()
            self.stdout.write(self.style.SUCCESS(f"Groups {group_names} successfully deleted"))
        else:
            content_type = ContentType.objects.get_for_model(Post)
            all_permissions = Permission.objects.filter(content_type=content_type)

            for name in group_names:
                name = name.lower()

                try:
                    group = Group.objects.create(name=name)
                    self.stdout.write(self.style.SUCCESS(f"Group {name} created"))

                    if name == 'editor':
                        group_perms = [perm for perm in all_permissions if 'add' not in perm.codename]
                        group.permissions.set(group_perms)

                    elif name == 'viewer':
                        group_perms = [perm for perm in all_permissions if 'view' in perm.codename]
                        group.permissions.set(group_perms)

                    elif name == 'author':
                        group_perms = [perm for perm in all_permissions if 'view' in perm.codename
                                       and 'add' in perm.codename]
                        group.permissions.set(group_perms)

                    else:
                        self.stdout.write(self.style.WARNING(f"Group {name} is not supported"))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Group {name} already exists"))
