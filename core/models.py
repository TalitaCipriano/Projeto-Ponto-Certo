# core/models.py
from django.db import models

class Categoria(models.Model):
    """Modelo para categorizar produtos, como 'Eletrônicos' ou 'Roupas'."""
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="URL amigável (ex: eletronicos)")
    
    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome

class Produto(models.Model):
    """Modelo para os itens do mercado."""
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',) # Ordena por nome por padrão

    def __str__(self):
        return self.nome

