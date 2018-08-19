Your answers to the questions go here.

# Datadog Coding Challenge - Bradley Shields

## Format Testing - Embedding Images:

To be sure I knew how to embed my screenshots, and that the formatting would be correct, I created the repository [datadog_test](https://github.com/bradleyjay/datadog_test). I tried two methods to embed images from github's "Mastering Markdown" [guide.](https://guides.github.com/features/mastering-markdown/)

1. Absolute github path

```![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)``` 

This works, but that's not necessarily a static URL. Depending on the branch referenced, that URL grows to include the branch name, and "tree". That's risky as things change in the repo.

2. Relative github path

``` ![GitHub Logo](/images/tormund.jpg)```


In this case, a relative path works better because it moves with the README.md in a given branch, which in this case is where I'm embedding the image.

Check complete! There's our fearless leader, Tormund Giantsbane (ginger beards of the world, unite!) Now, to set up the enviornment for the Coding Challenge.

*Note: on macOS, to screenshot, use Shift+CMD+4*


## Prerequisites - Setup the Enviornment

#### Initial VM Install and Launch

Having used Docker briefly before, I was curious to learn about Vagrant. I followed the [guide](https://www.vagrantup.com/intro/getting-started/) for setting up a Vagrant Virtual Machine(VM) project:
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

 gave me access to this box. I then commented out the previous ```config.vm.box``` line for to deselect Ubuntu 12.04 LTS. This version of the virtual box was already running, so a ```vagrant destroy``` was used to remove that instance of the virtual machine. 

 I then ran a ```vagrant up```, which downloaded the new 16.04 LTS box and started our new server. Finally, ```vagrant ssh``` brought me into the new version of the box. Upon launch, there is a message about Ubuntu 18.04.1 LTS being available, but for now I'll use this version unless I find stability or dependency issues. The Ubuntu 16.04 LTS box has *many* more downloads, so the odds seem good that it's a stable release, despite being a daily build.


#### Datadog Agent Setup

As instructed, I signed up for Datadog as a "Datadog Recruiting Candidate", then informed Datadog about my stack (Python, MySQL, GitHub, Slack). For the Agent Setup, I chose Ubuntu (since we'll be using our VM, not my local macOS), and applied the provided command to our Vagrant box:

```DD_API_KEY=8677a7b08834961d73c4e0e22dbd6e07 bash -c "$(curl -L https://raw.githubusercontent.com/DataDog/datadog-agent/master/cmd/agent/install_script.sh)"```

After a number of get, unpack, and install calls, the Datadog Agent reported it was running and functioning properly. For reference, the installer reported at the end:

    If you ever want to stop the Agent, run:

        ```sudo systemctl stop datadog-agent```

    And to run it again run:

        ```sudo systemctl start datadog-agent```


## Collecting Metrics

Now, the assignment.

1. **Add tags in the Agent config file and show us a screenshot of your host and its tags on the Host Map page in Datadog.**

#### Step 1: Find the Agent config file
At this point, I went to the Datadog [overview](https://docs.datadoghq.com/) documentation, and opened up the Agent section. Selecting [Ubuntu](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/) and reading down the page, the Agent config file location is listed. Looking through the Datadog Agent Installer output in my VM terminal window, I could see Agent V6 was installed, not V5. The Agent config file is therefore located at ```/etc/datadog-agent/datadog.yaml```.

