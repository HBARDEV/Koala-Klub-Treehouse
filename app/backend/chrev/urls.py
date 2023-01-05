from django.urls import path
from chrev import chrevViews
app_name='chrev'

urlpatterns = [





	
	
	#Apps

	path('post_details/',chrevViews.post_details,name="post-details"),

	path('email_compose/',chrevViews.email_compose,name="email-compose"),
	path('email_inbox/',chrevViews.email_inbox,name="email-inbox"),
	path('email_read/',chrevViews.email_read,name="email-read"),

	#Calender
	path('app_calender/',chrevViews.app_calender,name="app-calender"),
	#shop
	path('ecom_checkout/',chrevViews.ecom_checkout,name="ecom-checkout"),
	path('ecom_customers/',chrevViews.ecom_customers,name="ecom-customers"),
	path('ecom_invoice/',chrevViews.ecom_invoice,name="ecom-invoice"),
	path('ecom_product_detail/',chrevViews.ecom_product_detail,name="ecom-product-detail"),
	path('ecom_product_grid/',chrevViews.ecom_product_grid,name="ecom-product-grid"),
	path('ecom_product_list/',chrevViews.ecom_product_list,name="ecom-product-list"),
	path('ecom_product_order/',chrevViews.ecom_product_order,name="ecom-product-order"),
	
	#charts
	path('chart_chartist/',chrevViews.chart_chartist,name="chart-chartist"),
	path('chart_chartjs/',chrevViews.chart_chartjs,name="chart-chartjs"),
	path('chart_flot/',chrevViews.chart_flot,name="chart-flot"),
	path('chart_morris/',chrevViews.chart_morris,name="chart-morris"),
	path('chart_peity/',chrevViews.chart_peity,name="chart-peity"),
	path('chart_sparkline/',chrevViews.chart_sparkline,name="chart-sparkline"),

	#Components
	#---->Bootstrap
	path('ui_accordion/',chrevViews.ui_accordion,name="ui-accordion"),
	path('ui_alert/',chrevViews.ui_alert,name="ui-alert"),
	path('ui_badge/',chrevViews.ui_badge,name="ui-badge"),
	path('ui_button/',chrevViews.ui_button,name="ui-button"),
	path('ui_modal/',chrevViews.ui_modal,name="ui-modal"),
	path('ui_button_group/',chrevViews.ui_button_group,name="ui-button-group"),
	path('ui_list_group/',chrevViews.ui_list_group,name="ui-list-group"),
	path('ui_media_object/',chrevViews.ui_media_object,name="ui-media-object"),
	path('ui_card/',chrevViews.ui_card,name="ui-card"),
	path('ui_carousel/',chrevViews.ui_carousel,name="ui-carousel"),
	path('ui_dropdown/',chrevViews.ui_dropdown,name="ui-dropdown"),
	path('ui_popover/',chrevViews.ui_popover,name="ui-popover"),
	path('ui_progressbar/',chrevViews.ui_progressbar,name="ui-progressbar"),
	path('ui_tab/',chrevViews.ui_tab,name="ui-tab"),
	path('ui_typography/',chrevViews.ui_typography,name="ui-typography"),
	path('ui_pagination/',chrevViews.ui_pagination,name="ui-pagination"),
	path('ui_grid/',chrevViews.ui_grid,name="ui-grid"),

	#Components
	#---->Plugins
	path('uc_select2/',chrevViews.uc_select2,name="uc-select2"),
	path('uc_nestable/',chrevViews.uc_nestable,name="uc-nestable"),
	path('uc_noui_slider/',chrevViews.uc_noui_slider,name="uc-noui-slider"),
	path('uc_sweetalert/',chrevViews.uc_sweetalert,name="uc-sweetalert"),
	path('uc_toastr/',chrevViews.uc_toastr,name="uc-toastr"),
	path('map_jqvmap/',chrevViews.map_jqvmap,name="map-jqvmap"),
	path('uc_lightgallery/',chrevViews.uc_lightgallery,name="uc-lightgallery"),
	#Widget Basic
	path('widget_basic/',chrevViews.widget_basic,name="widget-basic"),
	#forms
	path('form_element/',chrevViews.form_element,name="form-element"),
	path('form_wizard/',chrevViews.form_wizard,name="form-wizard"),
	path('form_ckeditor/',chrevViews.form_ckeditor,name="form-ckeditor"),
	path('form_pickers/',chrevViews.form_pickers,name="form-pickers"),
	path('form_validation_jquery/',chrevViews.form_validation_jquery,name="form-validation-jquery"),

	#table
	path('table_bootstrap_basic/',chrevViews.table_bootstrap_basic,name="table-bootstrap-basic"),
	path('table_datatable_basic/',chrevViews.table_datatable_basic,name="table-datatable-basic"),
	
	#Pages
	path('page_register/',chrevViews.page_register,name="page-register"),
	path('page_login/',chrevViews.page_login,name="page-login"),
	path('page_error_400/',chrevViews.page_error_400,name="page-error-400"),
	path('page_error_403/',chrevViews.page_error_403,name="page-error-403"),
	path('page_error_404/',chrevViews.page_error_404,name="page-error-404"),
	path('page_error_500/',chrevViews.page_error_500,name="page-error-500"),
	path('page_error_503/',chrevViews.page_error_503,name="page-error-503"),
	path('page_lock_screen/',chrevViews.page_lock_screen,name="page-lock-screen"),
	path('page_forgot_password/',chrevViews.page_forgot_password,name="page-forgot-password")
	

]
