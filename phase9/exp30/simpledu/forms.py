from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, DataRequired, URL, NumberRange
import email_validator
from simpledu.models import db, User, Course


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3, 24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24, '密码长度要在6~24个字符之间')])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_emil(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')



class CourseForm(FlaskForm):
    name = StringField('coursename', validators=[DataRequired(), Length(5, 32)])
    description = TextAreaField('coursedescripe', validators=[DataRequired(), Length(20, 256)])
    image_url = StringField('image', validators=[DataRequired(), URL()])
    author_id = IntegerField('authorID', validators=[DataRequired(), NumberRange(min=1, message='invalidID')])
    submit = SubmitField('submit')

    def validate_author_id(self, field):
        if not User.query.get(field.data):
            raise ValidationError('user not exist')

    def create_course(self):
        course = Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course
