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
* plotDial.py<br>
 Yala
* plotLongitudinalCorrection.py<br>
 A Sundial never gives the same time as your watch.  
* plotAnalemma.py<br>
 Yala
 
## How to Assemble in Affinity Designer

Follow book instructions for your ware, but I use [Affinity Designer](https://affinity.serif.com/en-us/designer/).

## What to Change in the Scripts for _Your_ Project

