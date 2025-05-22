import bleach

from config import settings


class BleachSanitizerMixin:
    """
    Nous allons créer une classe de mixin pour reutiliser dans tout nos serializers pour nettoyer les champs de type HTML.
    Protèger les champs de type HTML contre les attaques XSS.
    """

    def sanitize_input(self, key, value):
        if key in getattr(settings, "BLEACH_EXCLUDE_FIELDS", []):
            return value
        if isinstance(value, str):
            # Utiliser bleach pour nettoyer le texte
            return bleach.clean(
                value,
                tags=getattr(settings, "BLEACH_ALLOWED_TAGS", []),
                attributes=getattr(settings, "BLEACH_ALLOWED_ATTRIBUTES", {}),
                strip=True
            )
        elif isinstance(value, dict):
            # Si la valeur est un dictionnaire, nettoyer chaque valeur
            return {k: self.sanitize_input(k, v) for k, v in value.items()}
        elif isinstance(value, list):
            # Si la valeur est une liste, nettoyer chaque élément
            return [self.sanitize_input(key, v) for v in value]
        return value

    def to_internal_value(self, data):
        cleaned_data = {}
        for key, value in data.items():
            cleaned_data[key] = self.sanitize_input(key, value)
        return super().to_internal_value(cleaned_data)
