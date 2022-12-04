from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile/', views.profile),
    path('reslog/', views.reslog),
    path('FAQ/', views.fuck),
    path('payment/', views.payment),

    path('english/', views.english),
    path('english/wordlevel/', views.englishWordlevel),
    path('english/sentence/', views.englishSentence),
    path('english/grammar/', views.englishGrammar), 
    path('english/speaking/', views.englishSpeaking),
    path('english/article/', views.englishArticle),

    path('ict/', views.ict),
    path('ict/introduction/', views.ictIntro),
    path('ict/variables/', views.ictVar),
    path('ict/conditions/', views.ictIfelse),
    path('ict/array/', views.ictArray),
    path('ict/oop/', views.ictOOP),
    path('ict/quiz/', views.ictQuiz),

    path('math/', views.math),
    path('math/calculus1/', views.mathCalcOne),
    path('math/calculus2/', views.mathCalcTwo),
    path('math/discrete-math/', views.mathDisc),
    path('math/linear-algebra/', views.mathLinear),
    path('math/geometry/', views.mathGeo),

    path('physics/', views.physics),
    path('physics/atomic-physics/', views.physicsAtom),
    path('physics/electricity-and-magnetism/', views.physicsElect),
    path('physics/mechanics/', views.physicsMech),
    path('physics/optics/', views.physicsOptics),
    path('physics/thermodynamics/', views.physicsThermo),
]