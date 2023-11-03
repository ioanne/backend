from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class CustomLoginView(LoginView):
    template_name = "custom_login.html"

    def form_valid(self, form):
        messages.success(self.request, "Inicio de sesión exitoso.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Credenciales incorrectas. Por favor, inténtalo de nuevo."
        )  # Mensaje de error
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    pass
