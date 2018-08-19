Your answers to the questions go here.

# Datadog Coding Challenge - Bradley Shields

## Workspace Prep Work: Setup
### Format Testing - Embedding Images:

To be sure I knew how to embed my screenshots, and that the formatting would be correct, I created the repository [datadog_test](https://github.com/bradleyjay/datadog_test). I tried two methods to embed images from github's "Mastering Markdown" [guide.](https://guides.github.com/features/mastering-markdown/)

1. Absolute github path

```![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)``` 

This works, but that's not necessarily a static URL. Depending on the branch referenced, that URL grows to include the branch name, and "tree". That's risky as things change in the repo.

2. Relative github path

``` ![GitHub Logo](/images/tormund.jpg)```


In this case, a relative path works better because it moves with the README.md in a given branch, which in this case is where I'm embedding the image.

Check complete! There's our fearless leader, Tormund Giantsbane (ginger beards of the world, unite!) Now, to set up the enviornment for the Coding Challenge.

*Note: on macOS, to screenshot, use Shift+CMD+4*


### Virtual Environment

#### Initial Install and Launch

I followed the [guide](https://www.vagrantup.com/intro/getting-started/) for setting up a Vagrant Virtual Machine(VM) project:
- Downloaded and installed [Vagrant](https://www.vagrantup.com/downloads.html) 2.1.2 for macOS.
- Per Vagrant's recommendation, updated my [VirtualBox](https://www.virtualbox.org/wiki/Downloads) install to 5.2.18. 

Then, I tested launching the VM via

    vagrant init hashicorp/precise64
    vagrant up 

And accessed the VM via ```vagrant ssh```. We're in, great news.

#### VM Customization

With our VM up and running, that's great, but the DataDog coding challenge specifically recommends running Ubuntu v.16.04. By default, Vagrant VM boots into Ubuntu 12.04 LTS. Let's change that to ensure our dependencies are in-line for the Datadog Agent.

Vagrant base images are called "boxes," and cloning one is how a VirtualBox environment is chosen. From the [Box Catalog](https://app.vagrantup.com/boxes/search?page=1&provider=virtualbox&q=ubuntu+16.04&sort=downloads&utf8=%E2%9C%93) I found [Ubuntu 16.04 LTS](https://app.vagrantup.com/ubuntu/boxes/xenial64). Adding the ```config.vm.box``` line to our Vagrantfile like so:

    Vagrant.configure("2") do |config|
       config.vm.box = "ubuntu/xenial64"
    end

 gave me access to this box. I then commented out the previous ```config.vm.box``` line for Ubuntu 12.04 LTS.


