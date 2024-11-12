import asyncio
import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_google_search():
    async with async_playwright() as p:
        browser = await p.firefox.launch(
            headless=False
        )
        page = await browser.new_page()
        await page.goto("https://google.com")
        await page.locator('[aria-label="Найти"]').fill("Автотесты")
        await page.get_by_label("Поиск в Google").first.click()
        await expect(page).to_have_title("Автотесты - Поиск в Google")
        await expect(page.locator('[class="logo"]')).to_be_visible()
        await expect(page.locator('[class="MjjYud"]')).not_to_have_count(0)
        await expect(page.locator('[class="NKTSme"]')).not_to_have_count(0)
        await expect(page.locator('[aria-label="Очистить"]')).to_be_visible()
        await page.get_by_label("Очистить").click()
        await expect(page.locator('[class="gLFyf"]')).to_be_empty()
        await asyncio.sleep(15)
        await browser.close()


asyncio.run(test_google_search())
