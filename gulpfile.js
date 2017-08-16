'use strict';
 
const gulp = require('gulp');
const rename = require('gulp-rename');
const autoprefixer = require('gulp-autoprefixer');
const sass = require('gulp-sass');
const exec = require('child_process').exec;

gulp.task('start', () => {
    exec('python manage.py runserver', function (err, stdout, stderr) {});
    gulp.watch('./static/sass/*.scss', ['sass']);
});

gulp.task('sass', () => {
    gulp.src('./static/sass/main.scss')
    .pipe(autoprefixer({
        browsers: ['last 2 versions'],
        cascade: false
    }))
    .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('./static/css'));
});