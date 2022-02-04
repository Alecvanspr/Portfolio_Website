using Microsoft.AspNetCore.Mvc;

public class SpotifyController: Controller{
    public IActionResult Index(){
        return View();
    }
}