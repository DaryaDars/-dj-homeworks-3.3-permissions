from rest_framework import permissions

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет полный доступ только создателю объекта.
    Остальным — только чтение (GET, HEAD, OPTIONS).
    """
    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Запись (редактирование/удаление) разрешена только создателю (creator)
        return obj.creator == request.user