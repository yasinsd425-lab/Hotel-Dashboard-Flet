import flet as ft

def main(page: ft.Page):
    # --- تنظیمات صفحه ---
    page.title = "HotelOps Executive"
    page.theme_mode = "dark"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#000000"
    
    # تنظیم اسکرول برای کل صفحه جهت جلوگیری از گیر کردن
    page.scroll = "auto"

    # --- استایل‌های شیشه‌ای (FIXED COLORS) ---
    # به جای ft.colors.with_opacity از کدهای هگز استفاده کردیم
    # فرمت: #AARRGGBB (دو رقم اول آلفا یا شفافیت است)
    glass_bg = "#B3101216"      # معادل 0.7 opacity
    card_glass = "#801A1D24"    # معادل 0.5 opacity
    border_color = "#4DFFFFFF"  # معادل 0.3 opacity white
    accent_color = "cyan"
    text_muted = "#B0B3B8"
    
    # رنگ‌های کمکی برای badges
    badge_colors = {
        "green": "#334CAF50",  # Green 20% opacity
        "orange": "#33FF9800", # Orange 20% opacity
        "red": "#33F44336"     # Red 20% opacity
    }

    # --- داده‌های ساختگی ---
    properties_data = [
        {"name": "The St Kilda Esplanade", "loc": "Melbourne", "occ": "94%", "rev": "$24,500", "pnl": "+12%", "status": "Clean Data"},
        {"name": "Sydney Harbour View", "loc": "Sydney", "occ": "88%", "rev": "$31,200", "pnl": "+8%", "status": "Clean Data"},
        {"name": "Gold Coast Resort", "loc": "Gold Coast", "occ": "98%", "rev": "$45,000", "pnl": "+15%", "status": "Xero Sync"},
        {"name": "Adelaide Heritage", "loc": "Adelaide", "occ": "76%", "rev": "$12,400", "pnl": "-2%", "status": "Review Needed"},
        {"name": "Perth City Center", "loc": "Perth", "occ": "82%", "rev": "$18,900", "pnl": "+5%", "status": "Clean Data"},
        {"name": "Brisbane River Suites", "loc": "Brisbane", "occ": "91%", "rev": "$22,100", "pnl": "+9%", "status": "Mews Audit"},
        {"name": "Hobart Waterfront", "loc": "Tasmania", "occ": "85%", "rev": "$15,600", "pnl": "+4%", "status": "Clean Data"},
    ]

    # --- توابع کمکی UI ---
    def create_status_badge(status):
        # انتخاب رنگ ساده
        color_name = "green" if "Clean" in status else "orange" if "Sync" in status else "red"
        bg_color_hex = badge_colors[color_name]
        
        return ft.Container(
            content=ft.Text(status, size=11, weight="bold", color="white"),
            bgcolor=bg_color_hex,
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            border_radius=15,
            border=ft.border.all(1, color_name)
        )

    def create_kpi_card(title, value, subtext, icon, trend_up=True):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(icon, color=accent_color if trend_up else "red", size=28),
                    bgcolor="#33000000", # Black 20%
                    padding=12, border_radius=12
                ),
                ft.Column([
                    ft.Text(title, size=12, color=text_muted, weight="w500"),
                    ft.Text(value, size=22, weight="bold", color="white"),
                    ft.Row([
                        ft.Icon("trending_up" if trend_up else "trending_down",
                               color="green" if trend_up else "red", size=14),
                        ft.Text(subtext, size=11, color="green" if trend_up else "red")
                    ], spacing=2)
                ], spacing=2)
            ], spacing=15),
            bgcolor=card_glass,
            padding=15,
            border_radius=15,
            expand=True,
            border=ft.border.all(1, border_color),
            # بلور را حذف کردم چون در وب گاهی سنگین است، اما اگر خواستی بگذار باشد
        )

    def create_mini_chart(label, value_height):
        return ft.Column([
            ft.Container(width=20, height=value_height, bgcolor=accent_color, border_radius=3),
            ft.Text(label, size=10)
        ], horizontal_alignment="center")

    # --- محتوای صفحات ---
    def get_overview_content():
        rows = []
        for p in properties_data:
            rev_number = float(p['rev'].replace('$', '').replace(',', ''))
            revpar = rev_number / 100
            rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Row([ft.Icon("apartment", size=16, color=text_muted), ft.Text(p['name'] , weight="bold")])),
                    ft.DataCell(ft.Text(p['loc'])),
                    ft.DataCell(ft.Text(p['occ'], color="green" if int(p['occ'].strip('%')) > 80 else "orange")),
                    ft.DataCell(ft.Text(p['rev'])),
                    ft.DataCell(ft.Text(f"${revpar:.1f}", color=accent_color, weight="bold")),
                    ft.DataCell(create_status_badge(p['status'])),
                ])
            )
        
        return ft.Column([
            ft.Text("Portfolio Overview (7 Properties)", size=22, weight="bold"),
            ft.Divider(color="transparent", height=10),
            ft.Row([
                create_kpi_card("Total Revenue (AUD)", "$169,700", "Daily Aggr.", "attach_money"),
                create_kpi_card("Avg. Occupancy", "87.7%", "+2% vs Last Wk", "hotel"),
                create_kpi_card("Data Health", "98%", "Formulas Optimized", "dns"),
            ], spacing=20, wrap=True), # Wrap اضافه شد برای موبایل
            
            ft.Divider(color="transparent", height=20),
            
            ft.Text("Weekly Revenue Trend", size=14, color=text_muted),
            ft.Row([
                create_mini_chart("Mon", 40),
                create_mini_chart("Tue", 70),
                create_mini_chart("Wed", 50),
                create_mini_chart("Thu", 90),
                create_mini_chart("Fri", 100),
            ], alignment="center", spacing=20),
            
            ft.Divider(color="transparent", height=20),
            
            ft.Container(
                content=ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("PROPERTY")),
                        ft.DataColumn(ft.Text("LOCATION")),
                        ft.DataColumn(ft.Text("OCC %"), numeric=True),
                        ft.DataColumn(ft.Text("DAILY REV"), numeric=True),
                        ft.DataColumn(ft.Text("RevPAR", color=accent_color)),
                        ft.DataColumn(ft.Text("STATUS")),
                    ],
                    rows=rows,
                    heading_row_height=40,
                    data_row_min_height=55,
                    vertical_lines=ft.border.BorderSide(0, "transparent"),
                    horizontal_lines=ft.border.BorderSide(1, "#1AFFFFFF"), # Fixed color
                    column_spacing=20
                ),
                bgcolor=card_glass, border_radius=15, padding=20, border=ft.border.all(1, border_color),
                scroll="auto" # اسکرول افقی برای جدول
            )
        ], scroll="auto", expand=True)

    def get_pnl_content():
        return ft.Column([
            ft.Row([
                ft.Text("P&L Framework", size=22, weight="bold"),
                ft.FilledButton("Sync Xero", icon="sync", style=ft.ButtonStyle(bgcolor="green"))
            ], alignment="spaceBetween"),
            ft.Divider(color="transparent", height=10),
            ft.Container(
                content=ft.Column([
                    ft.Text("Consolidated Profit & Loss - AUD", weight="bold", size=16),
                    ft.Divider(color="white", opacity=0.1),
                    ft.Row([ft.Text("Total Revenue"), ft.Text("$1,240,000", weight="bold")], alignment="spaceBetween"),
                    ft.Row([ft.Text("COGS"), ft.Text("($320,000)", color="red")], alignment="spaceBetween"),
                    ft.Divider(color="white", opacity=0.1),
                    ft.Row([ft.Text("Net Operating Profit", size=18, color=accent_color), ft.Text("$510,000", size=18, weight="bold", color=accent_color)], alignment="spaceBetween"),
                ], spacing=15),
                bgcolor=card_glass, padding=30, border_radius=15, border=ft.border.all(1, border_color)
            )
        ], expand=True, scroll="auto")

    def get_framework_content():
        pipeline = ft.Container(
            content=ft.Row([
                ft.Column([ft.Icon("input", color="cyan"), ft.Text("Raw Data")]),
                ft.Icon("arrow_forward", color=text_muted),
                ft.Column([ft.Icon("memory", color="cyan"), ft.Text("Python Logic")]),
                ft.Icon("arrow_forward", color=text_muted),
                ft.Column([ft.Icon("dashboard", color="cyan"), ft.Text("Flet UI")]),
            ], alignment="center", spacing=30, wrap=True),
            bgcolor="#1AFFFFFF", # Fixed color
            padding=20, border_radius=15, border=ft.border.all(1, border_color)
        )
        return ft.Column([
            ft.Text("System Architecture", size=22, weight="bold"),
            ft.Divider(height=10, color="transparent"),
            pipeline,
            ft.Divider(height=20, color="transparent"),
            ft.Text("Optimizations:", color=text_muted),
            ft.ListTile(leading=ft.Icon("check", color="green"), title=ft.Text("Hex-Code Rendering"), subtitle=ft.Text("Optimized for web deployment compatibility.")),
        ], expand=True, scroll="auto")

    # --- ساختار اصلی ---
    content_area = ft.Container(content=get_overview_content(), expand=True, padding=30)

    def change_view(e):
        idx = e.control.selected_index
        if idx == 0: content_area.content = get_overview_content()
        elif idx == 1: content_area.content = get_pnl_content()
        elif idx == 2: content_area.content = get_framework_content()
        page.update()

    sidebar = ft.NavigationRail(
        selected_index=0,
        label_type="all",
        min_width=100,
        bgcolor="#CC08090C", # Fixed color
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(icon="dashboard", label="Overview"),
            ft.NavigationRailDestination(icon="pie_chart", label="P&L"),
            ft.NavigationRailDestination(icon="settings", label="System"),
        ],
        on_change=change_view
    )

    page.add(
        ft.Stack([
            ft.Image(src="https://images.unsplash.com/photo-1542314831-068cd1dbfeeb", width=1400, height=950, fit=ft.ImageFit.COVER, opacity=0.4),
            ft.Container(gradient=ft.LinearGradient(colors=["#CC000000", "#E6101216"]), expand=True),
            ft.Row([sidebar, ft.VerticalDivider(width=1, color="#1AFFFFFF"), content_area], expand=True)
        ], expand=True)
    )

if __name__ == "__main__":
    ft.app(target=main)
