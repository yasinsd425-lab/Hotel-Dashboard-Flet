import flet as ft

def main(page: ft.Page):
    # --- 1. تنظیمات صفحه (ساده و مطمئن) ---
    page.title = "HotelOps Dashboard"
    page.theme_mode = "dark"
    page.bgcolor = "#111111" # رنگ مشکی مات (بدون عکس)
    page.padding = 20
    page.scroll = "auto" # اسکرول اصلی صفحه روشن

    # --- 2. پالت رنگ (کاملاً سالید و بدون شفافیت) ---
    # استفاده از رنگ‌های تخت برای اطمینان از نمایش در وب
    bg_card = "#1E1E1E" 
    text_white = "#FFFFFF"
    text_gray = "#AAAAAA"
    accent = "#00E5FF" # فیروزه‌ای
    
    # --- 3. داده‌ها ---
    data = [
        ["St Kilda", "Melb", "94%", "$24,500", "Clean"],
        ["Sydney View", "Syd", "88%", "$31,200", "Clean"],
        ["Gold Coast", "GC", "98%", "$45,000", "Syncing"],
        ["Adelaide", "Adl", "76%", "$12,400", "Review"],
        ["Perth City", "Per", "82%", "$18,900", "Clean"],
        ["Brisbane", "Bri", "91%", "$22,100", "Audit"],
    ]

    # --- 4. توابع سازنده ---
    def create_card(title, value, icon):
        return ft.Container(
            content=ft.Column([
                ft.Icon(icon, color=accent, size=30),
                ft.Text(title, size=12, color=text_gray),
                ft.Text(value, size=24, weight="bold", color=text_white),
            ]),
            bgcolor=bg_card,
            padding=20,
            border_radius=10,
            expand=True, # این باعث می‌شود در موبایل و دسکتاپ درست پر شود
        )

    # --- 5. ساختار جدول (ساده‌ترین حالت ممکن) ---
    # تبدیل داده‌ها به ردیف‌های جدول
    table_rows = []
    for item in data:
        # محاسبه ساده RevPAR
        rev = float(item[3].replace("$","").replace(",",""))
        revpar = f"${rev/100:.0f}"
        
        # تعیین رنگ وضعیت
        status_color = "green" if item[4] == "Clean" else "orange"
        
        table_rows.append(
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(item[0], weight="bold")),
                ft.DataCell(ft.Text(item[1])),
                ft.DataCell(ft.Text(item[2])),
                ft.DataCell(ft.Text(item[3])),
                ft.DataCell(ft.Text(revpar, color=accent)), # ستون مهندسی
                ft.DataCell(ft.Container(
                    content=ft.Text(item[4], color="white", size=10),
                    bgcolor=status_color, padding=5, border_radius=5
                )),
            ])
        )

    # --- 6. چیدمان نهایی (بدون Stack، بدون پیچیدگی) ---
    
    # هدر
    header = ft.Column([
        ft.Text("Executive Dashboard", size=30, weight="bold", color="white"),
        ft.Text("Real-time Hotel Portfolio Performance", color=text_gray),
        ft.Divider(color="transparent", height=20),
    ])

    # ردیف کارت‌ها
    kpi_section = ft.Row([
        create_card("TOTAL REVENUE", "$169,700", "attach_money"),
        create_card("OCCUPANCY", "88.2%", "hotel"),
        create_card("SYSTEM HEALTH", "STABLE", "dns"),
    ], spacing=10, wrap=True) # wrap=True یعنی در موبایل زیر هم بروند

    # بخش جدول
    # نکته کلیدی: استفاده از ListView برای اسکرول افقی جدول در وب
    table_section = ft.Container(
        content=ft.Column([
            ft.Text("Property Performance", size=18, weight="bold", color="white"),
            ft.Row(
                [
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("HOTEL")),
                            ft.DataColumn(ft.Text("LOC")),
                            ft.DataColumn(ft.Text("OCC")),
                            ft.DataColumn(ft.Text("REV")),
                            ft.DataColumn(ft.Text("RevPAR")),
                            ft.DataColumn(ft.Text("STATUS")),
                        ],
                        rows=table_rows,
                        heading_row_color="#222222",
                        data_row_min_height=50,
                        border=ft.border.all(1, "#333333"),
                        vertical_lines=ft.border.BorderSide(0, "transparent"),
                    )
                ],
                scroll="auto" # این خط طلایی است: اسکرول افقی برای جدول می‌سازد
            )
        ]),
        bgcolor=bg_card,
        padding=20,
        border_radius=10,
        margin=ft.margin.only(top=20)
    )

    # افزودن همه به صفحه به صورت مستقیم
    page.add(
        header,
        kpi_section,
        table_section
    )

if __name__ == "__main__":
    ft.app(target=main)
