using System.Collections;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using iTextSharp.text.pdf;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using tcc.Models;
using tcc.Utils;

namespace tcc.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class PdfController : ControllerBase
    {
        [HttpGet]
        public List<PdfRetorno> Verificar()
        {
            List<PdfRetorno> retorno = new List<PdfRetorno>();
            retorno.Add(new PdfRetorno { Valor=1.23, Descricao = "Pao" });
            retorno.Add(new PdfRetorno { Valor=12.23, Descricao = "Cafe" });

            return retorno;
        }

        [HttpPost]
        public string Anexar(IFormFile file)
        {
            var extension = Path.GetExtension(file.FileName);
            var fileName = Path.GetFileNameWithoutExtension(file.FileName);

            Image image = Image.FromStream(file.OpenReadStream());

            var t = new Bitmap(image);

            for(int x = 0; x < t.Width; x++)
            {
                for(int y = 0; y < t.Height; y++)
                {
                    Color pixelColor = t.GetPixel(x, y);
                    Color newColor = Color.FromArgb(pixelColor.R, 0, 0);
                    t.SetPixel(x, y, newColor);
                }
            }



            return "OK";
        }
    }
}