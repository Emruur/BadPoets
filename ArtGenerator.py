from diffusers import StableDiffusionPipeline
import torch

class StableDiffusionArtGenerator:
    def __init__(self, model_id="CompVis/stable-diffusion-v1-4"):
        """
        Initializes the Stable Diffusion pipeline.
        
        Args:
            model_id: The model ID for Stable Diffusion (from Hugging Face).
        """
        self.pipe = StableDiffusionPipeline.from_pretrained(model_id)
        self.pipe = self.pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    def generate_art(self, prompt: str):
        """
        Generates art based on the given prompt.

        Args:
            prompt: The text prompt to generate art from.

        Returns:
            A PIL Image object of the generated art.
        """
        image = self.pipe(prompt).images[0]
        return image


if __name__ == "__main__":
    art_generator = StableDiffusionArtGenerator()
    prompt = """
    A peaceful sunset over a mountain range with glowing skies and calm waters
    """
    generated_image = art_generator.generate_art(prompt)
    generated_image.show()
