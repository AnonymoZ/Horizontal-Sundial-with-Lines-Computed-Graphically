# Horizontal Sundial with Lines Computed Graphically

Misse told us to build a Sundial for *Introduction to Astrophysics*, with no prior instruction. Here's how we did it!

Keep in mind these facts:
1. You need to design your Sundial according to your _Latitude_. Therefore, you can't just copy and paste mine!
2. Your Gnomon (the _triangle_!) needs to be constructed with _special_ angles. More on that later.
3. Your Sundial can also indicate the _day of the year_ (heck!). For that we need to include curves called _Analemma_.

Here's the finished product. There's more in our pdf (link)!


![Finished Sundial](https://i.imgur.com/uYcVIGa.jpg)

Yeah, I get it, the times do not match! I actually made a mistake in signs in the original code. The Dial is actually off by 17m11sec as calculated. Forgive!

## Begin

You can find all the theory that's required from this [book](https://www.amazon.com/Sundials-Theory-Construction-Albert-Waugh/dp/0486229475) (that's what I used):

<table> 
    <tr>
        <td>
            <img src="https://images-na.ssl-images-amazon.com/images/I/51kt5nWqYhL._SX313_BO1,204,203,200_.jpg" alt="alt text" width="170">
        </td>
    </tr> 
</table>

It'll tell you more on the _Analemma_, the Equation of Time, how to build your Gnomon and all you need to know to come up with and operate my code 😉

## Actually read the book!

At the complete end of the project, you're looking to produce a diagram like this:

![](https://i.imgur.com/UNu43jX.jpeg)

(You'll have to actually split the sheet into 2 if your Gnomon is thick, along the faint black vertical line if you can see, but that's explained in the book!)

I will assume you have read the book, but concepts you should have known I write them with Caps so you can still follow.

Disclaimer:<br> 
The code itself will not give you this image! Each script of code will give you _a piece_ of the image as a graphic (.svg). But you'll have to assemble all manually in Adobe Illustrator🤮, [Affinity Designer](https://affinity.serif.com/en-us/designer/)😁 or [Inkscape](https://inkscape.org/release/inkscape-1.1/)😏.
A next section shows you how.

And add a rectangle to know how to place Gnomon, and a faint black vertical line so you can split page!


## Which Script Does What

The exact reasoning behind the codes is in the pdf, but I gave you 3 scripts:
* **plot - Dial.py**<br><br>
 This is straightforward. The script gives you the face of a Sundial. <br>
 Red lines denote *Hours*, Blue lines denote *Half-Hours* and Yellow lines *Quarter-Hours*.<br>
 The fainter Grey lines are the minute lines.<br><br>
 The angles in the Dial have been calculated using the *Latitude* of your country.<br><br>
* **plot - LongitudinalCorrection.py**<br><br>
 A Sundial never gives the same time as your watch.<br><br>
 The time is off because of 2 reasons.<br><br>
 Different people will correct these _discrepancies_ differently. (I'm not saying, "..will correct these _errors_ differently." According to some people, the Sundial Time is the ultimate form of time and Clock Times are futility, but let us please keep all debates aside!)<br><br>
 One discrepancy your *Longitude* causes it. The Book tells you why, and by what value, but the discrepancy is constant. Every day of every year at every hour it is the same. The discrepancy says, "instead of reading the time 17:46, read it 10 minutes more late". Read 17:56, that is.<br>
 But instead of reading 5:50 then adding 10 minutes, why not call it 6:00 and paint it red instead! *[GIF Animation]*:<br><br>
 ![LC vs. Orig.](https://i.imgur.com/hCajgpy.gif)<br><br>
 The other discrepancy I'm afraid is uncorrectable by layman means. It is due to the *Equation of Time*. I have imagined that rotatable system would need be built with the hour lines made of magnetisable iron thin bars, made to attract or repel each other by a programmable electro-magnet. A system far beyond my intellectual means.<br>
 Let it be a purely intellectual pursuit, for truth be told, the amount of technology put into this correction, we're far better off using a good old digital watch!<br><br>
 Please note! You will use **plotLongitudinalCorrection.py** *instead* of **plotDial.py**. Because both give the same result, except that in one the lines are coloured differently.<br><br>
* **plot - Analemma.py**<br><br>
 The path the tip of the shadow will take during any day. These curves will have to be *carefully* placed on the Dial. This script only gives the curves, but using clever geometry, we will know exactly how to place 'em.<br><br> 
## How to Assemble in Affinity Designer

Follow book instructions for your ware, but I use [Affinity Designer](https://affinity.serif.com/en-us/designer/).<br><br>
How you place the curves on the Dial face makes use of this **Principle**. Of all the curves in the Analemma one is a straight line.<br><br>
We know the distance of this straight line from our Sundial's _Point of Convergence_. Which is the horizontal line on our Dial face where all hour lines converge.<br><br>
Code **plotAnalemma.py** even outputs the distance in Terminal. I used the formula featured prominently at the top of the Analemma's code:<br><br>
<code>The Distance of the Equinox line from Horizontal through Origin is 0.05568962772057622 metres.</code>


## What to Change in the Scripts for _Your_ Project

You can find beautiful colours for your project at [Coolors.co](https://coolors.co/palettes)! But we hope the colours that we chose were already beautiful enough! 😇
