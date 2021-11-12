import datetime
from django.shortcuts import redirect, render
from datetime import date

all_posts =[
    {'slug': 'hike-in-the-mountains',
    'image': 'mount.jpeg',
    'author': 'Agalo Simon',
    'title': 'Mountain Hiking',
    'date': date(2021,10,6),
    'excerpt': 'There is nothing important like views',
    'content': '''
    Lorem ipsum dolor, sit amet consectetur adipisicing elit.
         Ex, sit iste voluptatem exercitationem possimus dolores, 
         expedita, nam molestiae aliquam molestias temporibus nemo 
        ipsa dolorem reprehenderit placeat officia ipsum error incidunt?
        Lorem ipsum dolor, sit amet consectetur adipisicing elit.
         Ex, sit iste voluptatem exercitationem possimus dolores, 
         expedita, nam molestiae aliquam molestias temporibus nemo 
        ipsa dolorem reprehenderit placeat officia ipsum error incidunt?
        Lorem ipsum dolor, sit amet consectetur adipisicing elit.
         Ex, sit iste voluptatem exercitationem possimus dolores, 
         expedita, nam molestiae aliquam molestias temporibus nemo 
        ipsa dolorem reprehenderit placeat officia ipsum error incidunt?
    
    '''   
},

  {'slug': 'programming-is-fun',
    'image': 'coding.jpg',
    'author': 'Agalo Simon',
    'title': 'programming is fun',
    'date': date(2020,8,14),
    'excerpt': 'did you ever spend hours searching that one error in your code? the answer is yes!!! That what happend to me yesterday',
    'content': '''
    Lorem ipsum dolor, sit amet consectetur adipisicing elit.
         Ex, sit iste voluptatem exercitationem possimus dolores, 
         expedita, nam molestiae aliquam molestias temporibus nemo 
        ipsa dolorem reprehenderit placeat officia ipsum error incidunt?
        Lorem ipsum dolor, sit amet consectetur adipisicing elit.
         Ex, sit iste voluptatem exercitationem possimus dolores, 
         expedita, nam molestiae aliquam molestias temporibus nemo 
        ipsa dolorem reprehenderit placeat officia ipsum error incidunt?
        Lorem ipsum dolor, sit amet consectetur adipisicing elit.
         Ex, sit iste voluptatem exercitationem possimus dolores, 
         expedita, nam molestiae aliquam molestias temporibus nemo 
        ipsa dolorem reprehenderit placeat officia ipsum error incidunt?
    
    '''
  },

    {'slug': 'Into-the-woods',
    'image': 'nature.jpg',
    'author': 'Agalo Simon',
    'title': 'Nature at its best',
    'date': date(2019,10,29),
    'excerpt': 'Nature is amazing!! the amount of inspiration I get when i walk in nature is increadible',
    'content': '''
    Lorem ipsum dolor, sit amet consectetur adipisicing elit.
         Ex, sit iste voluptatem exercitationem possimus dolores, 
         expedita, nam molestiae aliquam molestias temporibus nemo 
        ipsa dolorem reprehenderit placeat officia ipsum error incidunt?
        Lorem ipsum dolor, sit amet consectetur adipisicing elit.
         Ex, sit iste voluptatem exercitationem possimus dolores, 
         expedita, nam molestiae aliquam molestias temporibus nemo 
        ipsa dolorem reprehenderit placeat officia ipsum error incidunt?
        Lorem ipsum dolor, sit amet consectetur adipisicing elit.
         Ex, sit iste voluptatem exercitationem possimus dolores, 
         expedita, nam molestiae aliquam molestias temporibus nemo 
        ipsa dolorem reprehenderit placeat officia ipsum error incidunt?
    
    '''
    }

]
# Create your views here.
def get_date(post):
    return post['date']
    # return post.get('date')



def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blogs/index.html', {
        'posts': latest_posts
    })



def posts(request):
    
    return render(request, 'blogs/allpost.html',{
        'all_posts': all_posts

    })
    


def post_details(request,slug):
    identify_posts = next(post for post in all_posts if post['slug']==slug)
    
    return render(request, 'blogs/post-details.html',{
        'post': identify_posts
    })

    
    