const main = document.querySelector(".main");
const categories = document.querySelector(".categories");
const themas = document.querySelector(".themes");
const URL_BASE = "http://localhost:8000";

async function searchCategoriesAndThemes() {
  const categoriesRequest = fetch(URL_BASE + "/flashcards/categories/");
  const themesResquest = fetch(URL_BASE + "/flashcards/themes/");

  await Promise.all([categoriesRequest, themesResquest])
    .then((responses) => {
      if (responses[0].status == 200 && responses[1].status == 200) {
        return Promise.all([responses[0].json(), responses[1].json()]);
      }
      throw new Error("Erro ao buscar categorias e temas");
    })
    .then((data) => {
      let categoriesData = data[0];
      let themesData = data[1];
      const themas = [];

      //for each para imprimir a categoria e os temas relacionados a ela
      categoriesData.forEach((category) => {
        if (category.category_name == "programação") {
          categories.innerHTML += `<div class="category">
                <h2 class="category_name">programação</h2>
              
                <div class="thema"><a class="disabled-link" href="#">Em breve</a></div>
                <div>
                  `;
          return;
        }
        let category_id = category.id;
        // for each para imprimir os temas relacionados a categoria
        themesData.forEach((theme) => {
          if (category_id == theme.category_id) themas.push(theme);
        });

        categories.innerHTML += `
          <div class="category">
            <h2 class="category_name">${category.category_name}</h2>
            <ul class="themes">
              
              ${themas
                .map((theme) => {
                  console.log(theme);
                  if (theme.category_id == category_id)
                    return `<div class="thema"><a href="cards.html?theme=${theme.id}">${theme.theme_name}</a> </div>`;
                })
                .join("")}
              
            </ul>
          </div>
        `;
      });
    })
    .catch((error) => {
      console.error(error);
    });
}
document.addEventListener("DOMContentLoaded", searchCategoriesAndThemes);
