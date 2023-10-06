using System.Collections;
using System.Collections.Generic;
using System.IO;
using Google.Cloud.Vision.V1;
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
        public List<string> Anexar(IFormFile file)
        {
            var extension = Path.GetExtension(file.FileName);
            var fileName = Path.GetFileNameWithoutExtension(file.FileName);

            Image image = Image.FromStream(file.OpenReadStream());

            List<string> lista = new List<string>();

            ImageAnnotatorClient client = ImageAnnotatorClient.Create();
            IReadOnlyList<EntityAnnotation> textAnnotations = client.DetectText(image);
            foreach (EntityAnnotation text in textAnnotations)
            {
                lista.Add($"Description: {text.Description}");
            }

            return lista;
        }
    }
}