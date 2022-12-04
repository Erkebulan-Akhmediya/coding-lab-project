import re
from django import views
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def reslog(request):
    return render(request, 'reslog.html')

def fuck(request):
    return render(request, 'FAQ.html')

def payment(request):
    return render(request, 'payment.html')


def english(request):
    return render(request, 'english/english.html')

def englishWordlevel(request):
    return render(request, 'english/wordlevel.html')

def englishSentence(request):
    return render(request, 'english/sentence.html')

def englishGrammar(request):
    return render(request, 'english/grammar.html')

def englishSpeaking(request):
    return render(request, 'english/speaking.html')

def englishArticle(request):
    return render(request, 'english/article.html')


def ict(request):
    return render(request, 'ict/ict.html')

def ictIntro(request):
    return render(request, 'ict/introduction.html')

def ictVar(request):
    return render(request, 'ict/variables.html')

def ictIfelse(request):
    return render(request, 'ict/ifelse.html')

def ictArray(request):
    return render(request, 'ict/array.html')

def ictOOP(request):
    return render(request, 'ict/oop.html')

def ictQuiz(request):
    return render(request, 'ict/quiz.html')


def math(request):
    return render(request, 'math/math.html')

def mathCalcOne(request):
    return render(request, 'math/calc.html')

def mathCalcTwo(request):
    return render(request, 'math/calc2.html')

def mathDisc(request):
    return render(request, 'math/disc.html')

def mathLinear(request):
    return render(request, 'math/linear.html')

def mathGeo(request):
    return render(request, 'math/geo.html')


def physics(request):
    return render(request, 'physics/phys.html')

def physicsAtom(request):
    return render(request, 'physics/atom.html')

def physicsElect(request):
    return render(request, 'physics/elect.html')

def physicsMech(request):
    return render(request, 'physics/mech.html')

def physicsOptics(request):
    return render(request, 'physics/optics.html')

def physicsThermo(request):
    return render(request, 'physics/thermo.html')