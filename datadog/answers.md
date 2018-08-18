Your answers to the questions go here.

# Datadog Coding Challenge - Bradley Shields

## Workspace Prep Work: Setup
### Format Testing - Embedding Images:

I wanted to be sure I knew how to embed my screenshots, and that the formatting would be correct. I created the repository datadog_test (https://github.com/bradleyjay/datadog_test), and tried two methods from github's "Mastering Markdown" [guide.](https://guides.github.com/features/mastering-markdown/)

1. Absolute github path

```![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)``` 

Works, but that's not necessarily a static URL. Depending on the branch referenced, that URL grows to include the branch name, and "tree". That's risky as things change in the repo.

2. Relative github path

``` ![GitHub Logo](/images/tormund.jpg)```


In this case, a relative path works better because it moves with the README.md in a given branch, which in this case is where I'm embedding the image.

Check complete! There's our fearless leader, Tormund Giantsbane (ginger beards of the world, unite!) Now for the Coding Challenge.

*Note: on macOS, to screenshot, use Shift+CMD+4*


### Virtual Environment

Followed the [guide](https://www.vagrantup.com/intro/getting-started/) to setting up a Vagrant VM project
- Downloaded and installed [Vagrant](https://www.vagrantup.com/downloads.html) 2.1.2 for macOS.
- Per Vagrant's recommendation, updated my VirtualBox [VirtualBox](https://www.virtualbox.org/wiki/Downloads) install to 5.2.18 for macOS. 

Then, I started the VM via

    vagrant init hashicorp/precise64
    vagrant up 

