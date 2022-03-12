using Microsoft.AspNetCore.Mvc;

public class WerkervaringController : Controller
    {

        public IActionResult Index()
        {
            return View();
        }
        public IActionResult Kippie(){
            return View();
        }

        public IActionResult KippieWinkelMedewerker(){
            return View();
        }
        public IActionResult KippieOrderPicker(){
            return View();
        }
        public IActionResult Jumbo(){
            return View();
        }
    }