from django.db.models.signals import post_save
from django.dispatch import receiver
from libraryapp.models import StaffUser
from django.contrib.auth.models import Group

@receiver(post_save, sender=StaffUser)
def ativu_staff(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user.is_staff = True
        user.save()
        
@receiver(post_save, sender=StaffUser)
def add_group_staff(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='Staffs')
        instance.user.groups.add(group)
    