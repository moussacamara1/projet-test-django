from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSelf(BasePermission):
    # L'utilisateur peut accéder à son propre profil et le modifier
    def has_object_permission(self, request, view, obj):
        return request.user == obj

    class IsAdminUserOrReadOnly(BasePermission):
        # Les admin peuvent tout faire et les autres utilisateurs peuvent seulement lire
        def has_permission(self, request, view):
            return request.method in SAFE_METHODS or request.user.is_staff
