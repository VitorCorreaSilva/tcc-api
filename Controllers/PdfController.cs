using System.Collections;
using System.Collections.Generic;
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
        public List<PdfRetorno> Anexar(IFormFile file)
        {
            var extension = Path.GetExtension(file.FileName);
            var fileName = Path.GetFileNameWithoutExtension(file.FileName);
            PdfParser pdfParser = new PdfParser();

            pdfParser.ExtractText(file.OpenReadStream(), fileName);

            List<PdfRetorno> retorno = new List<PdfRetorno>();
            retorno.Add(new PdfRetorno { Valor=1.23, Descricao = "Pao" });
            retorno.Add(new PdfRetorno { Valor=12.23, Descricao = "Cafe" });

            return retorno;
        }
    }
}