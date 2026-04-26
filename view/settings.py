WIDTH = 1920
HEIGHT = 1080
GEOMETRY = f"{WIDTH}x{HEIGHT}"

# Paleta principal do sistema
COLOR_BACKGROUND = "#0F1B16"    # Fundo escuro com leve tom verde
COLOR_CARD = "#18241C"          # Card escuro suave
COLOR_CARD_2 = "#213028"        # Card alternativo para blocos
COLOR_BORDER = "#436F4A"        # Borda verde suave
COLOR_SHADOW = "#0B140F"        # Sombra para profundidade

COLOR_TEXT = "#E9F3E9"          # Texto principal claro e confortável
COLOR_TEXT_MUTED = "#A2B3A2"    # Texto secundário mais suave
COLOR_WHITE = "#FFFFFF"         # Detalhes mais nítidos

# Cores temáticas agro
COLOR_PRIMARY = "#3E8E4A"       # Verde forte para botões principais
COLOR_SECONDARY = "#5AAE6D"     # Verde claro para hovers e destaques
COLOR_ACCENT = "#8AD8C6"        # Aqua suave para títulos e destaques
COLOR_HIGHLIGHT = "#F5B35D"     # Amarelo-dourado para pontos de atenção
COLOR_LINK = "#74B8E6"          # Azul claro para links e ações secundárias

# Cores de status
COLOR_SUCCESS = "#27AE60"       # Indicação positiva
COLOR_WARNING = "#E08A00"       # Indicação de alerta
COLOR_INFO = "#3498DB"          # Indicação informativa
COLOR_DANGER = "#E74C3C"        # Indicação de erro

# Funções utilitárias de cor

def get_status_color(status):
    key = status.strip().lower()
    return {
        "water": COLOR_INFO,
        "chuva": COLOR_INFO,
        "sun": COLOR_HIGHLIGHT,
        "sol": COLOR_HIGHLIGHT,
        "danger": COLOR_DANGER,
        "erro": COLOR_DANGER,
        "success": COLOR_SUCCESS,
        "ok": COLOR_SUCCESS,
        "warning": COLOR_WARNING,
        "aviso": COLOR_WARNING,
        "info": COLOR_INFO,
    }.get(key, COLOR_ACCENT)


def get_theme_colors(mode="dark"):
    if mode.strip().lower() == "light":
        return {
            "background": "#F3F7F1",
            "card": "#FFFFFF",
            "card_alt": "#DFECE0",
            "text": "#1F2A1F",
            "accent": COLOR_PRIMARY,
            "border": "#A2C1A0",
        }

    return {
        "background": COLOR_BACKGROUND,
        "card": COLOR_CARD,
        "card_alt": COLOR_CARD_2,
        "text": COLOR_TEXT,
        "accent": COLOR_ACCENT,
        "border": COLOR_BORDER,
    }


def blend_colors(color1, color2, factor=0.5):
    factor = max(0.0, min(1.0, factor))

    def hex_to_rgb(hex_str):
        hex_value = hex_str.lstrip("#")
        return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb):
        return "#" + "".join(f"{max(0, min(255, v)):02X}" for v in rgb)

    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    blended = tuple(int(round(rgb1[i] * (1 - factor) + rgb2[i] * factor)) for i in range(3))
    return rgb_to_hex(blended)
