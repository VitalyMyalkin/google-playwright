class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator('[aria-label="Найти"]')

    async def navigate(self):
        await self.page.goto("https://google.com")

    async def search(self, text):
        await self.search_term_input.fill(text)

    async def click_button(self):
        await self.page.get_by_label("Поиск в Google").first.click()
