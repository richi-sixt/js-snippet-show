//using selectors inside the element
const questions = document.querySelectorAll('.faq');

questions.forEach(function (question) {
  const btn = question.querySelector('.faq-btn');

  btn.addEventListener('click', function () {
    questions.forEach(function (item) {
      if (item !== question) {
        item.classList.remove('show-text');
      }
    });

    question.classList.toggle('show-text');
  });
});
