from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, Date, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    __tablename__ = {
        'comment' : 'Пользователи'
    }

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=True
    )

nickname = Column(String, comment='Никнейм', unique=True)
password = Column(String, comment='Пароль')
active = Column(Boolean, default=True, comment='Статус активен/заблокирован')
role = Column(String, comment='Роли')

recipes = relationship(comment='Рецепты', back_populates='author')
user_likes = relationship(comment='Лайки', back_populates='user')

def __repr__(self):
    return f'{self.id} {self.nickname} {self.password} {self.active} {self.role} {self.user.like}'

class Recipes_db(Base):
    __tablename__ = 'Recipes'
    __tablename__ = {
        'comment' : 'Рецепты'
    }

    id = Column(
       Integer,
       primary_key=True,
       autoincrement=True,
       unique=True,
       nullable=True
   )

recipe_name = Column(String(128), comment='Название рецепта')
description = Column(Text, comment='Описание рецепта')
cooking_steps = Column(Text, comment='Шаги приготовления')
photo = Column(String, comment='Фотография конечного блюда')
type = Column(String, comment='Тип блюда')
author_id = Column(Integer, ForeignKey("users.id"), comment='Автор')
active = Column(Boolean, comment='Статус', default=True)
date_of_creation = Column(Date, comment='Дата создания')

author = relationship(comment='Пользователи', back_populates='recipes')
recipe_likes = relationship(comment='Лайки', back_populates="recipe")
tags = relationship(comment='Хештеги рецептов', back_populates="recipe")

def __repr__(self):
    return f'{self.id} {self.recipe_name} {self.description} {self.cooking_steps} {self.photo} {self.type} {self.author_id} {self.active} {self.date_of_creation}{self.author} {self.recipe_likes} {self.tags}'

class Hashtag(Base):
    __tablename__ = 'hashtags'
    __tablename__ = {
        'comment' : 'Хештеги'
    }

id = Column(Integer, primary_key=True, index=True)
tag = Column(String, unique=True, index=True)

recipes = relationship(comment='Хештеги рецептов', back_populates='tag')

def __repr__(self):
    return f'{self. id} {self.tag} {self.recipes_db}'

class RecipeHashtag(Base):
    __tablename__ = 'Recipe hashtags'
    __table_args__ = (UniqueConstraint('tag_id', 'recipe_id', name='unique_tag'),)
    id = Column(Integer, primary_key=True, index=True)
    tag_id = Column(Integer, ForeignKey('hashtag.id'), index=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), index=True)

    tag = relationship(comment='Хештиг', back_populates='recipes')
    recipes = relationship(comment='Рецепт', back_populates='tag')

def __repr__(self):
    return f'{self.id} {self.tag_id} {self.recipe_id} {self.tag} {self.recipe}'

class Likes(Base):
    __tablename__ = 'Likes'
    __table_args__ = (UniqueConstraint('user_id', 'recipe_id', name='unique_likes'),)
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), index=True)

    recipes = relationship('Recipe', back_populates='recipe_likes')
    user = relationship('User', back_populates='user_likes')

    def __repr__(self):
        return f'{self.id} {self.user_id} {self.recipe_id} {self.recipes} {self.user}'