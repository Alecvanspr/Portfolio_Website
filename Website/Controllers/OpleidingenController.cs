using Microsoft.AspNetCore.Mvc;

public class OpleidingenController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
        public IActionResult MAVO(){
            return View();
        }
        public IActionResult MBO(){
            return View();
        }
        public IActionResult HBO(){
            return View();
        }
    }