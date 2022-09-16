from django.views import generic
from .forms import InquiryForm

class BlogView(generic.TemplateView):
    template_name = "blog.html"

class Blog_InquiryView(generic.FormView):
    template_name = "blog_inquiry.html"
    form_class = InquiryForm
