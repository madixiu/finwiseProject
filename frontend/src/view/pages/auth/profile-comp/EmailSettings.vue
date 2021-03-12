<template>
  <b-card>
    <!--begin::Header-->
    <div class="card-header py-3">
      <div class="card-title align-items-start flex-column">
        <b-card-title style="text-align:right">تنظیمات ایمیل</b-card-title>
        <b-card-sub-title style="text-align:right"
          >تغییرات ایمیل های دریافتی فین وایز</b-card-sub-title
        >
      </div>
      <div class="card-toolbar">
        <button type="reset" class="btn btn-success mr-2">ذخیره</button>
        <button type="reset" class="btn btn-secondary">لغو</button>
      </div>
    </div>
    <!--end::Header-->
    <!--begin::Form-->
    <form class="form">
      <div class="card-body">
        <div class="row">
          <label class="col-xl-12 col-md-12 col-xs-12"></label>
          <div class="col-xl-12 col-md-12 col-xs-12">
            <h5 class="font-weight-bold mb-6 text-right">ایمیل های دریافتی</h5>
          </div>
        </div>
        <div class="form-group row">
          <label
            class="col-xl-3 col-lg-3 col-md-3 col-xs-6 col-form-label text-right"
            >اطلاع رسانی از طریق ایمیل</label
          >
          <div class="col-lg-9 col-xl-9 col-md-9 col-xs-12">
            <span class="switch switch-sm">
              <label>
                <input type="checkbox" name="email_notification_1" />
                <span></span>
              </label>
            </span>
          </div>
        </div>
        <div class="form-group row">
          <label
            class="col-xl-3 col-lg-3 col-md-3 col-xs-6 col-form-label text-right"
            >ارسال کپی به ایمیل شخصی</label
          >
          <div class="col-lg-9 col-xl-9 col-md-9 col-xs-12">
            <span class="switch switch-sm">
              <label>
                <input type="checkbox" name="email_notification_2" />
                <span></span>
              </label>
            </span>
          </div>
        </div>
        <div class="separator separator-dashed my-10"></div>
        <div class="row">
          <label class="col-xl-12 col-md-12 col-xs-12"></label>
          <div class="col-xl-12 col-md-12 col-xs-12">
            <h5 class="font-weight-bold mb-6 text-right">موضوعات</h5>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >مواقع دریافت:</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class="checkbox-list">
              <label class="checkbox">
                <input type="checkbox" />
                <span></span> نوتیفیکشن جدید
              </label>
              <label class="checkbox">
                <input type="checkbox" />
                <span></span> اطلاعات سهم های مورد علاقه
              </label>
            </div>
          </div>
        </div>
        <div class="separator separator-dashed my-10"></div>
        <div class="row">
          <label class="col-xl-12 col-md-12 col-xs-12"></label>
          <div class="col-xl-12 col-md-12 col-xs-12">
            <h5 class="font-weight-bold mb-6 text-right">ایمیل های فین وایز</h5>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >موضوعات:</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class="checkbox-list">
              <label class="checkbox">
                <input type="checkbox" />
                <span></span> اطلاعات در مورد آپدیتهای جدید فینوایز
              </label>
              <label class="checkbox">
                <input type="checkbox" />
                <span></span> توضیحات و آموزش امکانات فینوایز
              </label>
              <label class="checkbox">
                <input type="checkbox" />
                <span></span> خبرنامه
              </label>
            </div>
          </div>
        </div>
      </div>
    </form>
    <!--end::Form-->
  </b-card>
</template>

<script>
export default {
  name: "EmailSettings"
};
</script>

<style scoped></style>
