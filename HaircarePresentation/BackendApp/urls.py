from django.urls import path
from BackendApp import views

urlpatterns = [

       path('index/',views.index,name="index"),
       path('Haircate/',views.Haircate,name="Haircate"),
       path('Hairdata/',views.Hairdata,name="Hairdata"),
       path('displayhair/',views.displayhair,name="displayhair"),
       path('edithair/<int:dataid>/',views.edithair,name="edithair"),
       path('hairupdate/<int:dataid>/',views.hairupdate,name="hairupdate"),
       path('hairdelete/<int:dataid>/',views.hairdelete,name="hairdelete"),
       path('hairpr/',views.hairpr,name="hairpr"),
       path('hairprbl_data/',views.hairprbl_data,name="hairprbl_data"),
       path('hair_problemdisplay/',views.hair_problemdisplay,name="hair_problemdisplay"),
       path('edit_hairproblem/<int:dataid>/',views.edit_hairproblem,name="edit_hairproblem"),
       path('hairproblem_upade/<int:dataid>/',views.hairproblem_upade,name="hairproblem_upade"),
       path('hairproblem_delete/<int:dataid>/',views.hairproblem_delete,name="hairproblem_delete"),
       path('brand/',views.brand,name="brand"),
       path('brand_data/',views.brand_data,name="brand_data"),
       path('displaybrand/',views.displaybrand,name="displaybrand"),
       path('brand_edit/<int:dataid>/',views.brand_edit,name="brand_edit"),
       path('brand_update/<int:dataid>/',views.brand_update,name="brand_update"),
       path('brand_delete/<int:dataid>/',views.brand_delete,name="brand_delete"),
       path('product_type/',views.product_type,name="product_type"),
       path('product_typedata/',views.product_typedata,name="product_typedata"),
       path('product_typedisplay/',views.product_typedisplay,name="product_typedisplay"),
       path('product_typeedit/<int:dataid>/',views.product_typeedit,name="product_typeedit"),
       path('producttype_update/<int:dataid>/',views.producttype_update,name="producttype_update"),
       path('producttype_delete/<int:dataid>/',views.producttype_delete,name="producttype_delete"),
       path('addproduct/',views.addproduct,name="addproduct"),
       path('product_data/',views.product_data,name="product_data"),
       path('adddisplay/',views.adddisplay,name="adddisplay"),
       path('addedit/<int:dataid>/',views.addedit,name="addedit"),
       path('addpro_update//<int:dataid>',views.addpro_update,name="addpro_update"),
       path('add_delete/<int:dataid>/',views.add_delete,name="add_delete"),
       path('adminlogin/',views.adminlogin,name="adminlogin"),
       path('admin_login/',views.admin_login,name="admin_login"),
       path('admin_logout/',views.admin_logout,name="admin_logout"),




       ]