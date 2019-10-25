# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class XzCart(models.Model):
    lid = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_cart'


class XzIndexCarousel(models.Model):
    cid = models.AutoField(primary_key=True)
    img = models.CharField(max_length=128, blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    href = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_index_carousel'


class XzIndexProduct(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    details = models.CharField(max_length=128, blank=True, null=True)
    pic = models.CharField(max_length=128, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    href = models.CharField(max_length=128, blank=True, null=True)
    seq_recommended = models.IntegerField(blank=True, null=True)
    seq_new_arrival = models.IntegerField(blank=True, null=True)
    seq_top_sale = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_index_product'


class XzLaptop(models.Model):
    lid = models.AutoField(primary_key=True)
    family_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    subtitle = models.CharField(max_length=128, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    promise = models.CharField(max_length=64, blank=True, null=True)
    spec = models.CharField(max_length=64, blank=True, null=True)
    lname = models.CharField(max_length=32, blank=True, null=True)
    os = models.CharField(max_length=32, blank=True, null=True)
    memory = models.CharField(max_length=32, blank=True, null=True)
    resolution = models.CharField(max_length=32, blank=True, null=True)
    video_card = models.CharField(max_length=32, blank=True, null=True)
    cpu = models.CharField(max_length=32, blank=True, null=True)
    video_memory = models.CharField(max_length=32, blank=True, null=True)
    category = models.CharField(max_length=32, blank=True, null=True)
    disk = models.CharField(max_length=32, blank=True, null=True)
    details = models.CharField(max_length=1024, blank=True, null=True)
    shelf_time = models.BigIntegerField(blank=True, null=True)
    sold_count = models.IntegerField(blank=True, null=True)
    is_onsale = models.IntegerField(blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_laptop'


class XzLaptopFamily(models.Model):
    fid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_laptop_family'


class XzLaptopPic(models.Model):
    pid = models.AutoField(primary_key=True)
    laptop_id = models.IntegerField(blank=True, null=True)
    sm = models.CharField(max_length=128, blank=True, null=True)
    md = models.CharField(max_length=128, blank=True, null=True)
    lg = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_laptop_pic'


class XzLogin(models.Model):
    uname = models.CharField(max_length=50, blank=True, null=True)
    upwd = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_login'


class XzOrder(models.Model):
    aid = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    order_time = models.BigIntegerField(blank=True, null=True)
    pay_time = models.BigIntegerField(blank=True, null=True)
    deliver_time = models.BigIntegerField(blank=True, null=True)
    received_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_order'


class XzOrderDetail(models.Model):
    did = models.AutoField(primary_key=True)
    order_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_order_detail'


class XzReceiverAddress(models.Model):
    aid = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    receiver = models.CharField(max_length=16, blank=True, null=True)
    province = models.CharField(max_length=16, blank=True, null=True)
    city = models.CharField(max_length=16, blank=True, null=True)
    county = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    cellphone = models.CharField(max_length=16, blank=True, null=True)
    fixedphone = models.CharField(max_length=16, blank=True, null=True)
    postcode = models.CharField(max_length=6, blank=True, null=True)
    tag = models.CharField(max_length=16, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_receiver_address'


class XzShoppingcartItem(models.Model):
    iid = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    is_checked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_shoppingcart_item'


class XzUser(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=32, blank=True, null=True)
    upwd = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    avatar = models.CharField(max_length=128, blank=True, null=True)
    user_name = models.CharField(max_length=32, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xz_user'
