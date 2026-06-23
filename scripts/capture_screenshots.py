import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
HTML_DIR = ROOT / "notebooks"
SCREENSHOT_DIR = ROOT / "submission" / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

def capture(html_filename, output_name, scroll_to_text=None, offset_y=-50, height=1200):
    html_path = HTML_DIR / html_filename
    if not html_path.exists():
        print(f"Error: {html_path} does not exist.")
        return
    
    print(f"Capturing screenshot for {html_filename}...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Setup page with a good width and height
        page = browser.new_page(viewport={"width": 1200, "height": height})
        page.goto(html_path.as_uri())
        page.wait_for_timeout(2000)  # Wait for page to render fully
        
        if scroll_to_text:
            try:
                # Find the heading or text block
                element = page.get_by_text(scroll_to_text).first
                if element:
                    element.scroll_into_view_if_needed()
                    # Apply offset if specified to center/top align better
                    page.evaluate(f"window.scrollBy(0, {offset_y})")
                    page.wait_for_timeout(1000)
            except Exception as e:
                print(f"Warning scrolling to '{scroll_to_text}': {e}")
        
        dest_path = SCREENSHOT_DIR / output_name
        page.screenshot(path=str(dest_path))
        print(f"Saved screenshot to {dest_path}")
        browser.close()

def main():
    # NB1: Vector index count + top-5 paraphrase query (we will start from Section 4)
    capture(
        html_filename="01_embeddings_index.html",
        output_name="nb1.png",
        scroll_to_text="4. TODO — embed + upsert toàn bộ corpus",
        offset_y=-30,
        height=1400
    )
    
    # NB2: Average Precision@10 table with hybrid > kw/sem
    capture(
        html_filename="02_hybrid_search_rrf.html",
        output_name="nb2.png",
        scroll_to_text="4. Đánh giá trên golden set",
        offset_y=-30,
        height=1100
    )
    
    # NB3: API response + P50/P95/P99 latency table
    capture(
        html_filename="03_search_api_benchmark.html",
        output_name="nb3.png",
        scroll_to_text="3. TODO — Latency benchmark",
        offset_y=-30,
        height=1250
    )
    
    # NB4: feast apply STDOUT + online lookup result + PIT join DF
    capture(
        html_filename="04_feast_feature_store.html",
        output_name="nb4.png",
        scroll_to_text="5. TODO — Batch latency benchmark",
        offset_y=-250,  # Scroll slightly up to capture section 3, 4, 5, 6, 7 in a tall window
        height=1600
    )

if __name__ == "__main__":
    main()
