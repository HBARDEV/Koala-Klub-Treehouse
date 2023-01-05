from django.shortcuts import  render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return render(request, "chrev/index.html")

@login_required
def index_2(request):
	return render(request, "chrev/index-2.html")

# @login_required
# def transactions(request):
# 	return render(request, "chrev/transactions.html")

# @login_required
# def coin_details(request):
# 	return render(request, "chrev/coin-details.html")

# @login_required
# def portfolio(request):
# 	return render(request, "chrev/portfolio.html")

# @login_required
# def market_capital(request):
# 	return render(request, "chrev/market-capital.html")



@login_required
def post_details(request):
	return render(request, "chrev/apps/post-details.html")

#email
@login_required
def email_compose(request):
	return render(request, "chrev/apps/email/email-compose.html")

@login_required
def email_inbox(request):
	return render(request, "chrev/apps/email/email-inbox.html")

@login_required
def email_read(request):
	return render(request, "chrev/apps/email/email-read.html")

@login_required
def app_calender(request):
	return render(request, "chrev/apps/app-calender.html")

#shop
@login_required
def ecom_checkout(request):
	return render(request, "chrev/apps/shop/ecom-checkout.html")

@login_required
def ecom_customers(request):
	return render(request, "chrev/apps/shop/ecom-customers.html")

@login_required
def ecom_invoice(request):
	return render(request, "chrev/apps/shop/ecom-invoice.html")

@login_required
def ecom_product_detail(request):
	return render(request, "chrev/apps/shop/ecom-product-detail.html")

@login_required
def ecom_product_grid(request):
	return render(request, "chrev/apps/shop/ecom-product-grid.html")

@login_required
def ecom_product_list(request):
	return render(request, "chrev/apps/shop/ecom-product-list.html")

@login_required
def ecom_product_order(request):
	return render(request, "chrev/apps/shop/ecom-product-order.html")

#charts
@login_required
def chart_chartist(request):
	return render(request, "chrev/charts/chart-chartist.html")

@login_required
def chart_chartjs(request):
	return render(request, "chrev/charts/chart-chartjs.html")

@login_required
def chart_flot(request):
	return render(request, "chrev/charts/chart-flot.html")

@login_required
def chart_morris(request):
	return render(request, "chrev/charts/chart-morris.html")

@login_required
def chart_peity(request):
	return render(request, "chrev/charts/chart-peity.html")

@login_required
def chart_sparkline(request):
	return render(request, "chrev/charts/chart-sparkline.html")

#Components
#---->Bootstrap
@login_required
def ui_accordion(request):
	return render(request, "chrev/bootstrap/ui-accordion.html")

@login_required
def ui_alert(request):
	return render(request, "chrev/bootstrap/ui-alert.html")

@login_required
def ui_badge(request):
	return render(request, "chrev/bootstrap/ui-badge.html")

@login_required
def ui_button(request):
	return render(request, "chrev/bootstrap/ui-button.html")

@login_required
def ui_modal(request):
	return render(request, "chrev/bootstrap/ui-modal.html")

@login_required
def ui_button_group(request):
	return render(request, "chrev/bootstrap/ui-button-group.html")

@login_required
def ui_list_group(request):
	return render(request, "chrev/bootstrap/ui-list-group.html")

@login_required
def ui_media_object(request):
	return render(request, "chrev/bootstrap/ui-media-object.html")

@login_required
def ui_card(request):
	return render(request, "chrev/bootstrap/ui-card.html")


@login_required
def ui_carousel(request):
	return render(request, "chrev/bootstrap/ui-carousel.html")


@login_required
def ui_dropdown(request):
	return render(request, "chrev/bootstrap/ui-dropdown.html")

@login_required
def ui_popover(request):
	return render(request, "chrev/bootstrap/ui-popover.html")

@login_required
def ui_progressbar(request):
	return render(request, "chrev/bootstrap/ui-progressbar.html")

@login_required
def ui_tab(request):
	return render(request, "chrev/bootstrap/ui-tab.html")

@login_required
def ui_typography(request):
	return render(request, "chrev/bootstrap/ui-typography.html")

@login_required
def ui_pagination(request):
	return render(request, "chrev/bootstrap/ui-pagination.html")

@login_required
def ui_grid(request):
	return render(request, "chrev/bootstrap/ui-grid.html")

#Plugins
@login_required
def uc_select2(request):
	return render(request, "chrev/plugins/uc-select2.html")

@login_required
def uc_nestable(request):
	return render(request, "chrev/plugins/uc-nestable.html")

@login_required
def uc_noui_slider(request):
	return render(request, "chrev/plugins/uc-noui-slider.html")

@login_required
def uc_sweetalert(request):
	return render(request, "chrev/plugins/uc-sweetalert.html")

@login_required
def uc_toastr(request):
	return render(request, "chrev/plugins/uc-toastr.html")

@login_required
def map_jqvmap(request):
	return render(request, "chrev/plugins/map-jqvmap.html")

@login_required
def uc_lightgallery(request):
	return render(request, "chrev/plugins/uc-lightgallery.html")


# Widget Basic
@login_required
def widget_basic(request):
	return render(request, "chrev/widget-basic.html")


#Forms

@login_required
def form_element(request):
	return render(request, "chrev/forms/form-element.html")

@login_required
def form_wizard(request):
	return render(request, "chrev/forms/form-wizard.html")

@login_required
def form_ckeditor(request):
	return render(request, "chrev/forms/form-ckeditor.html")


@login_required
def form_pickers(request):
	return render(request, "chrev/forms/form-pickers.html")

@login_required
def form_validation_jquery(request):
	return render(request, "chrev/forms/form-validation-jquery.html")

#Table
@login_required
def table_bootstrap_basic(request):
	return render(request, "chrev/table/table-bootstrap-basic.html")

@login_required
def table_datatable_basic(request):
	return render(request, "chrev/table/table-datatable-basic.html")

#pages
@login_required
def page_register(request):
	return render(request, "chrev/pages/page-register.html")

@login_required
def page_login(request):
	return render(request, "chrev/pages/page-login.html")

@login_required
def page_error_400(request):
	return render(request, "400.html")

@login_required
def page_error_403(request):
	return render(request, "403.html")

@login_required
def page_error_404(request):
	return render(request, "404.html")

@login_required
def page_error_500(request):
	return render(request, "500.html")

@login_required
def page_error_503(request):
	return render(request, "503.html")

@login_required
def page_lock_screen(request):
	return render(request, "chrev/pages/page-lock-screen.html")

@login_required
def page_forgot_password(request):
	return render(request, "chrev/pages/page-forgot-password.html")






