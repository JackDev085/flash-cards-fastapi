class Flashcard {
  constructor(question, answer, id) {
    this.question = question;
    this.answer = answer;
    this.id = id;
  }

  getQuestion() {
    return this.question;
  }

  getAnswer() {
    return this.answer;
  }

  setQuestion(question) {
    this.question = question;
  }

  setAnswer(answer) {
    this.answer = answer;
  }

  setId(id) {
    this.id = id;
  }

  getId() {
    return this.id;
  }
}
