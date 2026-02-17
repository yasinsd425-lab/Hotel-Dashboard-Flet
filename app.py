import flet as ft

def main(page: ft.Page):
    # --- 1. تنظیمات صفحه ---
    page.title = "HotelOps Executive"
    page.theme_mode = "dark"
    page.padding = 0
    page.spacing = 0
    # رنگ پس‌زمینه لوکس (سرمه‌ای/مشکی خیلی تیره) به جای عکس سنگین
    page.bgcolor = "#0E0E10" 
    page.scroll = None # اسکرول صفحه خاموش (کانتنت اسکرول دارد)

    # --- 2. پالت رنگ (Hex Safe) ---
    card_bg = "#1F1F22"       # رنگ کارت‌ها (مات و فلت)
    border_color = "#33FFFFFF" 
    accent_color = "#00F0FF"  # سایان نئونی
    text_muted = "#8A8A93"
    
    badge_green = "#1F3A25"
    badge_orange = "#3A2E1F"
    badge_red = "#3A1F1F"

    # --- 3. داده‌ها ---
    properties_data = [
        {"name": "St Kilda Esp.", "loc": "Melb", "occ": "94%", "rev": "$24,500", "status": "Clean Data"},
        {"name": "Sydney View", "loc": "Syd", "occ": "88%", "rev": "$31,200", "status": "Clean Data"},
        {"name": "Gold Coast", "loc": "GC", "occ": "98%", "rev": "$45,000", "status": "Xero Sync"},
        {"name": "Adelaide Her.", "loc": "Adl", "occ": "76%", "rev": "$12,400", "status": "Review"},
        {"name": "Perth City", "loc": "Per", "occ": "82%", "rev": "$18,900", "status": "Clean Data"},
        {"name": "Brisbane Riv.", "loc": "Bri", "occ": "91%", "rev": "$22,100", "status": "Mews Audit"},
        {"name": "Hobart Pier", "loc": "Tas", "occ": "85%", "rev": "$15,600", "status": "Clean Data"},
    ]

    # --- 4. کامپوننت‌ها ---
    def create_status_badge(status):
        if "Clean" in status: bg, b_col, t_col = badge_green, "green", "#4CAF50"
        elif "Sync" in status: bg, b_col, t_col = badge_orange, "orange", "#FF9800"
        else: bg, b_col, t_col = badge_red, "red", "#F44336"
            
        return ft.Container(
            content=ft.Text(status, size=10, weight="bold", color=t_col),
            bgcolor=bg,
            padding=ft.Padding(8, 4, 8, 4),
            border_radius=4, # گوشه‌های کمی تیزتر (مدرن‌تر)
            border=ft.Border.all(1, bg) # بدون بوردر رنگی جیغ
        )

    def create_kpi_card(title, value, subtext, icon, trend_up=True):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(icon, color=text_muted, size=20),
                    ft.Text(title, size=11, color=text_muted, weight="w600"),
                ]),
                ft.Text(value, size=24, weight="bold", color="white"),
                ft.Row([
                    ft.Icon("trending_up" if trend_up else "trending_down",
                           color=accent_color if trend_up else "red", size=14),
                    ft.Text(subtext, size=11, color=accent_color if trend_up else "red")
                ], spacing=4)
            ], spacing=10),
            bgcolor=card_bg,
            padding=20, 
            border_radius=12,
            expand=True,
            border=ft.Border.all(1, "#333333") # بوردر خیلی ظریف
        )

    def create_mini_chart(label, value_height):
        return ft.Column([
            ft.Container(width=12, height=value_height, bgcolor=accent_color, border_radius=2),
            ft.Text(label, size=9, color=text_muted)
        ], horizontal_alignment="center", spacing=4)

    # --- 5. محتوای Overview ---
    def get_overview_content():
        rows = []
        for p in properties_data:
            rev_num = float(p['rev'].replace('$', '').replace(',', ''))
            revpar = rev_num / 100
            rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(p['name'], weight="bold", size=13)),
                    ft.DataCell(ft.Text(p['loc'], size=13)),
                    ft.DataCell(ft.Text(p['occ'], size=13)),
                    ft.DataCell(ft.Text(p['rev'], size=13)),
                    ft.DataCell(ft.Text(f"${revpar:.0f}", color=accent_color, weight="bold", size=13)),
                    ft.DataCell(create_status_badge(p['status'])),
                ])
            )
            
        return ft.Column([
            ft.Text("Executive Overview", size=28, weight="bold", color="white"),
            ft.Text("Real-time Hotel Performance Metrics", size=13, color=text_muted),
            ft.Divider(height=25, color="transparent"),
            
            # KPI Section
            ft.Row([
                create_kpi_card("TOTAL REVENUE", "$169,700", "+12.5%", "attach_money"),
                create_kpi_card("AVG OCCUPANCY", "88.2%", "+2.1%", "hotel"),
                create_kpi_card("SYSTEM HEALTH", "98.9%", "Stable", "dns"),
            ], spacing=15),
            
            ft.Divider(height=25, color="transparent"),
            
            # Chart + Table Section
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Weekly Trends", size=14, weight="bold", color="white"),
                        ft.Row([
                            create_mini_chart("M", 25), create_mini_chart("T", 50),
                            create_mini_chart("W", 35), create_mini_chart("T", 70),
                            create_mini_chart("F", 90)
                        ], spacing=8)
                    ], alignment="spaceBetween"),
                    
                    ft.Divider(height=15, color="transparent"),
                    
                    # جدول با اسکرول ایمن
                    ft.Row([
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("PROPERTY", color=text_muted)),
                                ft.DataColumn(ft.Text("LOC", color=text_muted)),
                                ft.DataColumn(ft.Text("OCC", color=text_muted)),
                                ft.DataColumn(ft.Text("REV", color=text_muted)),
                                ft.DataColumn(ft.Text("RevPAR", color=accent_color)),
                                ft.DataColumn(ft.Text("STATUS", color=text_muted)),
                            ],
                            rows=rows,
                            heading_row_height=40,
                            data_row_min_height=50,
                            vertical_lines=ft.border.BorderSide(0, "transparent"),
                            horizontal_lines=ft.border.BorderSide(1, "#222222"),
                            column_spacing=20
                        )
                    ], scroll="auto")
                ]),
                bgcolor=card_bg, padding=25, border_radius=12,
                border=ft.Border.all(1, "#333333")
            )
        ], scroll="hidden", expand=True) # اسکرول مخفی برای زیبایی

    # --- 6. محتوای Framework ---
    def get_framework_content():
        return ft.Column([
            ft.Text("Architecture", size=28, weight="bold"),
            ft.Divider(height=30, color="transparent"),
            ft.Container(
                content=ft.Row([
                    ft.Column([ft.Icon("input", color=accent_color), ft.Text("Xero/Mews")]),
                    ft.Icon("arrow_forward", color=text_muted),
                    ft.Column([ft.Icon("memory", color=accent_color), ft.Text("Python Core")]),
                    ft.Icon("arrow_forward", color=text_muted),
                    ft.Column([ft.Icon("dashboard", color=accent_color), ft.Text("Flet UI")]),
                ], alignment="center", spacing=30, wrap=True),
                bgcolor=card_bg, padding=40, border_radius=12,
                border=ft.Border.all(1, "#333333")
            )
        ], expand=True)

    # --- 7. ساختار اصلی (بدون Stack، بدون عکس) ---
    # این ساختار 100% امن است و سفید نمی‌شود
    
    content_area = ft.Container(content=get_overview_content(), expand=True, padding=30)

    def change_view(e):
        idx = e.control.selected_index
        if idx == 0: content_area.content = get_overview_content()
        elif idx == 1: content_area.content = get_framework_content()
        page.update()

    sidebar = ft.NavigationRail(
        selected_index=0,
        label_type="all",
        min_width=90,
        bgcolor="#0A0A0C", # کمی تیره‌تر از پس‌زمینه
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(icon="dashboard", label="Dash"),
            ft.NavigationRailDestination(icon="settings", label="System"),
        ],
        on_change=change_view
    )

    page.add(
        ft.Row(
            [
                sidebar, 
                ft.VerticalDivider(width=1, color="#222222"), 
                content_area
            ], 
            expand=True # این خط حیاتی است
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
