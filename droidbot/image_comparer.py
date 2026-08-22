class ImageComparer:
    @staticmethod
    def compareImage(before_image_path, after_image_path):
        from .GeminiAI import GeminiAi
        import PIL.Image

        if GeminiAi.is_disabled():
            return None

        try:
            image1 = PIL.Image.open(before_image_path)
            image2 = PIL.Image.open(after_image_path)
            prompt = [
                "Describe the key visual differences between these two images. Focus on changes in objects, colors, and overall composition. I am mainly searching if this two page is identical or not. So if you find any type of dissimilarity ans yes otherwise no. By anytype i mean at the app screen not the system bar of the phone. Ans me in only yes or no. Give me response as a json. The json should contain 2 things. For example the dissimilarity is a toast message that contains Password must be 8 character long. But if both pages are completely different page in that case consider as a pass. Because the navigation took place. So You should create a json like {verditc: fail, response: Password must be 8 character long} here verdict will be the tone of the response like it's negative or positive. Positive means pass and negative means fail. Also if the 2nd image contain a new page image then it should consider as a pass and response should be 'Navigation occured'.",
                image1,
                image2,
            ]
            return GeminiAi.generate_content(prompt, timeout=20)
        except FileNotFoundError:
            print("Error: Image files not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
