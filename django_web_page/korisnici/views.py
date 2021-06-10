from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, TaskCategory,CustomKorisnici,Comment
from .forms import PostForm, updatePost, CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .encryption_util import *
# LIKE VIEW
def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


# NAVBAR
def NavFooter(request):
    return render(request, "nav_footer.html", {})


def is_valid_queryparam(param):
    return param != '' and param is not None  # uslov za pretragu



# POST CATEGORY
def PostPerCategory(request, pk):  # Funkcija sa prikaz postova po kategoriji pk is ID categorije koji se prosledjuje preko URLa.
    posts = Post.objects.all()  # Dohvatamo sve postove
    category = TaskCategory.objects.filter(pk=pk)  # Filtriramo po category ID
    posts = posts.filter(task_category__in=category)  # Prikazujemo samo postove iz izabrane kategorije

    context = {
        'posts': posts,
        'category': category,
    }

    return render(request, "post_category.html", context)





# POST PAGE VIEW
def PostPageView(request):
    posts = Post.objects.all()  # model Post iz baze, object.all- sve sto taj model sadrzi
    category = TaskCategory.objects.all()  # model TasjCategiry
    context = {  # stavljamo u listu koje modele cemo da koristimo u html file i njihov naziv
        'posts': posts,
        'category': category,
    }
    category = request.GET.get('category')  # poreko get requesta uzimamo podatke iz forme i njenih polja
    # cenaMin = request.GET.get('cenaMin')
    cenaMax = request.GET.get('cenaMax')

    if is_valid_queryparam(category) and category != 'Choose...':  # uslov za pretragu po kategoriji
        posts = posts.filter(task_category__category_title=category)  # filtriramo podatke u bazi za Post, po category
        category = TaskCategory.objects.all()
        context = {
            'posts': posts,
            'category': category,
        }
        return render(request, "post_page.html", context)  # html stranica koja sluzi za prikaz podataka


    if is_valid_queryparam(cenaMax):  # pretraga po polju budget
        posts = posts.filter(budget__lt=cenaMax)  # detalji prikaza, da se sortira od najnize do selektovane max cene u formi
        category = TaskCategory.objects.all()
        context = {
            'posts': posts,
            'category': category,
        }
        return render(request, "post_page.html", context)  # prikaz ako se odredi max cena

    return render(request, "post_page.html", context)  # ako cena nije odrednjena

# def get_queryset(self):
#     return Post.objects.filter(category_id=self.kwargs.get('pk'))


# POST PAGE VIEW
def MyPosts(request):
    posts = Post.objects.all()  # model Post iz baze, object.all- sve sto taj model sadrzi
    category = TaskCategory.objects.all()  # model TaskCategory
    context = {  # stavljamo u listu koje modele cemo da koristimo u html file i njihov naziv
        'posts': posts,
        'category': category,
    }
    category = request.GET.get('category')  # poreko get requesta uzimamo podatke iz forme i njenih polja
    return render(request, "my-posts2.html", context)  # ako cena nije odrednjena

def MyPosts2(request):
    posts = Post.objects.all()  # model Post iz baze, object.all- sve sto taj model sadrzi
    category = TaskCategory.objects.all()  # model TaskCategory
    context = {  # stavljamo u listu koje modele cemo da koristimo u html file i njihov naziv
        'posts': posts,
        'category': category,
    }
    category = request.GET.get('category')  # poreko get requesta uzimamo podatke iz forme i njenih polja
    return render(request, "my-posts.html", context)  # ako cena nije odrednjena

# def get_queryset(self):
#     return Post.objects.filter(category_id=self.kwargs.get('pk'))


# POST DETAIL VIEW
class PostDetail(DetailView):  # DetailView biblioteka koja sluzi za odredjeni prikaz ili polje iz baze
    model = Post
    template_name = 'post_detail.html'
	
    def get_context_data(self, *args,**kwargs):
        context = super(PostDetail,self).get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        context['total_likes'] = total_likes
        return context




# HOME PAGE VIEW
class PostHomeView(ListView):
    model = TaskCategory
    context_object_name = 'cat'
    template_name = 'home.html'  # html stranica na kojoj ce podaci biti prikazani
    # oredering = ['category_title']      #sortitamo kategorije prema azbucnom redu, takodje je prikazano i u na drugi nacin u sledeceoj funkciji

    def get_queryset(self):  # get_queryset biblioteka iz paythona
        return TaskCategory.objects.order_by(
            'category_title')  # order_by sortiranje po task_title koloni, sa [:9] prikaza iz baze(odredjujemo koliko ce stvari iz baze biti prikazano, ide po IDu te baze)

    def get_context_data(self, *args,**kwargs):
        cat_manu = TaskCategory.objects.order_by('category_title')
        context =super(PostHomeView, self).get_context_data(*args,**kwargs)
        context["cat_manu"] = cat_manu
        return context



#ADD POST PAGE
class AddPost(CreateView):  # CreateView biblioteka koja sluzi za unos podataka preko forme u bazu
    model = TaskCategory
    # context_object_name = 'post'
    form_class = PostForm  # forma odakle ce uzeti podatke za bazu
    template_name = 'add_post.html'  # html stranica na kojoj ce forma biti prikazana
    # fields = '__all__'
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.kwargs['pk']})
        return kwargs



# UPDATE POST
class UpdatePost(UpdateView):  # UpdateView, update je postojece podakte iz baze.
    model = Post
    context_object_name = 'post'
    form_class = updatePost
    template_name = 'update_post.html'
    success_url = reverse_lazy('my-posts')


# DELETE POST
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('my-posts')




#PROFILE PAGE VIEW
class ShowProfile(DetailView):
    model = CustomKorisnici
    context_object_name = 'profile'
    template_name = 'user_profile.html'


    def get_context_data(self, *args, **kwargs):
        users = CustomKorisnici.objects.all()
        context = super(ShowProfile, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(CustomKorisnici, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context



#MAJSTORI LIST PAGE VIEW
class MajstoriView(ListView):
    model = CustomKorisnici
    context_object_name = 'majstori'
    template_name = 'majstori_view.html'  # html stranica na kojoj ce podaci biti prikazani

    def get_queryset(self):  # get_queryset biblioteka iz paythona
        return CustomKorisnici.objects.filter(user_type=CustomKorisnici.MAJSTOR)




#MAJSTORI PROFILE PAGE VIEW
class MajstoriProfile(DetailView):  # DetailView biblioteka koja sluzi za odredjeni prikaz ili polje iz baze
    model = CustomKorisnici
    template_name = 'majstori_profile.html'
    def get_context_data(self, *args, **kwargs):
        users = CustomKorisnici.objects.all()
        context = super(MajstoriProfile, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(CustomKorisnici, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


#ADD COMMENT PAGE VIEW
class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs	
	
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', args=(self.kwargs['pk'],))
