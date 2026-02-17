import flet as ft

def main(page: ft.Page):
    # --- 1. تنظیمات صفحه ---
    page.title = "HotelOps Executive"
    page.theme_mode = "dark"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#000000"
    # نکته حیاتی: اسکرول صفحه اصلی خاموش، اسکرول فقط در کانتینر محتوا
    page.scroll = None 

    # --- 2. پالت رنگ (Hex Safe) ---
    glass_bg = "#CC101216"      # تیره شیشه‌ای
    card_glass = "#991A1D24"    # کارت شیشه‌ای
    border_color = "#33FFFFFF"  # بوردر محو
    accent_color = "cyan"
    text_muted = "#B0B3B8"
    
    badge_green = "#334CAF50"
    badge_orange = "#33FF9800"
    badge_red = "#33F44336"

    # --- 3. داده‌ها ---
    properties_data = [
        {"name": "St Kilda Esp.", "loc": "Melb", "occ": "94%", "rev": "$24,500", "status": "Clean Data"},
        {"name": "Sydney View", "loc": "Syd", "occ": "88%", "rev": "$31,200", "status": "Clean Data"},
        {"name": "Gold Coast", "loc": "GC", "occ": "98%", "rev": "$45,000", "status": "Xero Sync"},
        {"name": "Adelaide Her.", "loc": "Adl", "occ": "76%", "rev": "$12,400", "status": "Review"},
        {"name": "Perth City", "loc": "Per", "occ": "82%", "rev": "$18,900", "status": "Clean Data"},
        {"name": "Brisbane Riv.", "loc": "Bri", "occ": "91%", "rev": "$22,100", "status": "Mews Audit"},
    ]

    # --- 4. کامپوننت‌های UI ---
    def create_status_badge(status):
        if "Clean" in status: bg, b_col = badge_green, "green"
        elif "Sync" in status: bg, b_col = badge_orange, "orange"
        else: bg, b_col = badge_red, "red"
            
        return ft.Container(
            content=ft.Text(status, size=10, weight="bold", color="white"),
            bgcolor=bg,
            padding=ft.Padding(8, 4, 8, 4),
            border_radius=12,
            border=ft.Border.all(1, b_col)
        )

    def create_kpi_card(title, value, subtext, icon, trend_up=True):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(icon, color=accent_color if trend_up else "red", size=24),
                    bgcolor="#33000000", padding=10, border_radius=10
                ),
                ft.Column([
                    ft.Text(title, size=11, color=text_muted, weight="w500"),
                    ft.Text(value, size=20, weight="bold", color="white"),
                    ft.Row([
                        ft.Icon("trending_up" if trend_up else "trending_down",
                               color="green" if trend_up else "red", size=12),
                        ft.Text(subtext, size=10, color="green" if trend_up else "red")
                    ], spacing=2)
                ], spacing=2)
            ], spacing=10),
            bgcolor=card_glass,
            padding=15, border_radius=15, 
            expand=True, # در موبایل کل عرض را بگیرد
            border=ft.Border.all(1, border_color)
        )

    def create_mini_chart(label, value_height):
        return ft.Column([
            ft.Container(width=15, height=value_height, bgcolor=accent_color, border_radius=2),
            ft.Text(label, size=9, color=text_muted)
        ], horizontal_alignment="center", spacing=2)

    # --- 5. محتوای اصلی (Overview) ---
    def get_overview_content():
        rows = []
        for p in properties_data:
            rev_num = float(p['rev'].replace('$', '').replace(',', ''))
            revpar = rev_num / 100
            rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(p['name'], weight="bold", size=12)),
                    ft.DataCell(ft.Text(p['loc'], size=12)),
                    ft.DataCell(ft.Text(p['occ'], size=12)),
                    ft.DataCell(ft.Text(p['rev'], size=12)),
                    ft.DataCell(ft.Text(f"${revpar:.0f}", color=accent_color, weight="bold", size=12)),
                    ft.DataCell(create_status_badge(p['status'])),
                ])
            )
            
        return ft.Column([
            ft.Text("Executive Overview", size=24, weight="bold"),
            ft.Text("Real-time Portfolio Performance", size=12, color=text_muted),
            ft.Divider(height=15, color="transparent"),
            
            # KPI Cards
            ft.Row([
                create_kpi_card("Total Revenue", "$169k", "Daily Aggr.", "attach_money"),
                create_kpi_card("Occupancy", "87.7%", "+2% vs L.W.", "hotel"),
                create_kpi_card("System Health", "98%", "Stable", "dns"),
            ], spacing=15, wrap=True),
            
            ft.Divider(height=15, color="transparent"),
            
            # Chart Section
            ft.Container(
                content=ft.Row([
                    ft.Text("Weekly Trend", size=12, color=text_muted),
                    ft.Row([
                        create_mini_chart("M", 30), create_mini_chart("T", 60),
                        create_mini_chart("W", 40), create_mini_chart("T", 80),
                        create_mini_chart("F", 100)
                    ], spacing=10)
                ], alignment="spaceBetween"),
                bgcolor=card_glass, padding=15, border_radius=12, border=ft.Border.all(1, border_color)
            ),

            ft.Divider(height=15, color="transparent"),
            
            # Data Table (Safe Scrolling)
            ft.Container(
                content=ft.Row([
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("HOTEL")),
                            ft.DataColumn(ft.Text("LOC")),
                            ft.DataColumn(ft.Text("OCC")),
                            ft.DataColumn(ft.Text("REV")),
                            ft.DataColumn(ft.Text("RevPAR", color=accent_color)),
                            ft.DataColumn(ft.Text("STATUS")),
                        ],
                        rows=rows,
                        heading_row_height=35,
                        data_row_min_height=45,
                        vertical_lines=ft.border.BorderSide(0, "transparent"),
                        horizontal_lines=ft.border.BorderSide(1, "#1AFFFFFF"),
                        column_spacing=15
                    )
                ], scroll="auto"), # اسکرول افقی جدول
                bgcolor=card_glass, 
                border_radius=15, 
                padding=10,
                border=ft.Border.all(1, border_color)
            )
        ], scroll="auto", expand=True) # اسکرول عمودی محتوا

    # --- 6. محتوای دوم (Framework) ---
    def get_framework_content():
        return ft.Column([
            ft.Text("Architecture", size=22, weight="bold"),
            ft.Divider(height=20, color="transparent"),
            ft.Container(
                content=ft.Row([
                    ft.Column([ft.Icon("input", color="cyan"), ft.Text("Xero/Mews")]),
                    ft.Icon("arrow_forward", color=text_muted),
                    ft.Column([ft.Icon("memory", color="cyan"), ft.Text("Python")]),
                    ft.Icon("arrow_forward", color=text_muted),
                    ft.Column([ft.Icon("dashboard", color="cyan"), ft.Text("Flet UI")]),
                ], alignment="center", spacing=20, wrap=True),
                bgcolor=card_glass, padding=30, border_radius=15,
                border=ft.Border.all(1, border_color)
            )
        ], expand=True)

    # --- 7. ساختار اصلی (Layout) ---
    content_area = ft.Container(content=get_overview_content(), expand=True, padding=20)

    def change_view(e):
        idx = e.control.selected_index
        if idx == 0: content_area.content = get_overview_content()
        elif idx == 1: content_area.content = get_framework_content()
        page.update()

    sidebar = ft.NavigationRail(
        selected_index=0,
        label_type="all",
        min_width=80,
        bgcolor="#E608090C", # کمی شفاف
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(icon="dashboard", label="Dash"),
            ft.NavigationRailDestination(icon="settings", label="Sys"),
        ],
        on_change=change_view
    )

    # --- 8. ترکیب نهایی (Stack برای عکس پس زمینه) ---
    page.add(
        ft.Stack([
            # لایه ۱: عکس (با fit رشته‌ای برای جلوگیری از ارور)
            ft.Image(
                src="https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
                width=2000, # عرض زیاد برای اطمینان
                height=1500,
                fit="cover", 
                opacity=0.3
            ),
            # لایه ۲: گرادینت برای خوانایی
            ft.Container(gradient=ft.LinearGradient(colors=["#CC000000", "#CC101216"]), expand=True),
            
            # لایه ۳: محتوای اصلی (سایدبار + کانتنت)
            ft.Row([
                sidebar, 
                ft.VerticalDivider(width=1, color="#1AFFFFFF"), 
                content_area
            ], expand=True)
        ], expand=True)
    )

if __name__ == "__main__":
    ft.app(target=main)
