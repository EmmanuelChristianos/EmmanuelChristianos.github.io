---
layout: default
title: Network Infrastructure
parent: Blog
---

<style type="text/css">

#warningP {

	margin-left: 10px;
	margin-right: 10px;
	padding-bottom: 10px;
}

details {
	border-radius: 2px;
    background: #DEDFF6;
    color: black;
    margin-top: 10px;
    margin-bottom: 15px;


}

details summary {
    font-size: 17px;
    vertical-align: top;
    background: #7F61EF;
    color: #FFF;
    border-radius: 3px;
    padding: 2px 5px;
    outline: none;
    text-align: center;
}

details summary::-webkit-details-marker {
    display: none;
}

details[open] summary:before {
    background-position: -18px 0;
}

details[open] summary {
    background: #6C47EF;
    color: #fff;
}

</style>

# Networking Fundamentals
{: .no_toc .fs-9}

The Network Fundamentals Chapter has a corresponding Github repository which contains the resources used throughout the following chapter.
{: .fs-6 .fw-300 }

[View it on GitHub](https://github.com/EmmanuelChristianos/EmmanuelChristianos.github.io){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}


<div  markdown="1">
## Environment Setup
{: .fs-7.fw-400 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-0}

Networking Fundamentals follows a more theory based approach and doesn't involve a lot of practical content. Majority of the practical content that does appear in the following chapter will work regardless of the operating system you are using. However if you would like to be able to follow along exactly with the instructions detailed in this chapter then you should complete the steps in the [OS Setup](#os-setup){:.fs-4 .md-0 .mr-2 }page to replicate the environment that was used by the author.

{: .d-block}

### OS Setup
{: .fs-6 .fw-400 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-1}

The exercises in this chapter and their corresponding instructions have been completed on a Linux system. If you already are using Linux then you can move onto the [Application Installation](#application-installation){:.fs-4 .md-0 .mr-0 } section to install the required software.

If you are working on an OS other than Linux I will be detailing two ways to replicate the Linux environment used in this chapter. The first will be using [Docker](#docker-installation-and-setup){:.fs-4 .md-0 .mr-0 } and the second will be using [VirtualBox](#virtualbox-installation-and-setup){:.fs-4 .md-0 .mr-0 }. Both can be downloaded an set up on any major operating system.
{: .d-block}


### Docker or VirtualBox?
{: .fs-6 .fw-400 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-1}

Docker will only give you a command line to use and you will have to install the applications that will be used on your own computer. VirtualBox however will give you a Graphical User Interface (GUI) for the operating system you will download. You can install the applications that we will be using on either however for some application we will be using the GUI and so if you are using Docker you will have to download that specific application on your own computer. If you use VirtualBox you can download all the application needed onto the VirtualBox we set up. 
{: .d-block}

#### Docker Installation and Setup
{: .fs-5 .fw-200 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-2}


<details >

<summary> Warning: Instruction May Change! [click]</summary>

<p id="warningP">
(Warning: The following instructions might not accurately represent the steps that you need to undertake to install and setup docker.
</p>

<p id="warningP">
Dockers installation and set up process is subject to change by Docker and so the instructions below detail the steps to install and set up Docker at the time of making this chapter.
</p>

<p id="warningP">
It is highly unlikely that the Docker commands themselves will change. However the design on the website will likely change over time.
</p>

<p id="warningP">
If the following steps do not work for you then at the end of the steps there will be a more generalized guide to setting up Docker.)
</p>

</details>
{: .fs-4 .fw-400 }


1. Go to [Docker Website](www.docker.com){: .fs-4 .mb-4 .mb-md-0 } and click on the 'Get Started'
2. Click Docker Desktop 'Download for [Your OS]' (My OS was Mac as you can see in the photo below, yours might be Windows)
<img src="https://emmanuelchristianos.github.io//assets/images/networking/docker1.png">
3. Open the Docker.dmg file and move the docker icon into your application.
4. Go to your applications folder and open Docker
<details>
<summary> Warning: Unidentified Developer Solution [click]</summary>

<p id="warningP">
Some Mac users might receive a warning saying 'Docker' can't be opened because it is from  an unidentified developer. If this happens to you follow these steps:
</p>

<p id="warningP">
1. Open up 'Systems Preferences'
</p>

<p id="warningP">
2. Navigate to 'Security & Privacy'
</p>

<p id="warningP">
3. On the menu tab at the top of the system preferences screen click the 'General' tab
</p>

<p id="warningP">
4. At the bottom of the 'General' tab you should see the unidentified developer warning for docker with a button next to it that says 'Open Anyway' click 'Open Anyway'
</p>
</details>

<div markdown="1">
5
{: .fs-3 .d-inline-block .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; For Mac users open up the application named terminal (this can be found by searching 'terminal' in spotlight)
{: .d-inline}

Enter the following line into the terminal:
```shell
docker pull ubuntu
```
You should have something that looks like this
<img src="https://emmanuelchristianos.github.io//assets/images/networking/dockerpullubuntu.png">

Then enter the following:
```shell
docker run -it ubuntu
```
<img src="https://emmanuelchristianos.github.io//assets/images/networking/dockerrunubuntu.png">

You now have a Linux shell running on Ubuntu, if you type:
```shell
ls
```
you will see a list of all the files from the root directory
<img src="https://emmanuelchristianos.github.io//assets/images/networking/ubuntuls.png">

In the future when the Linux container is needed for an exercise you simply haven to:

1. Open the docker application from your application folder
2. Open up terminal
3. Type the following into terminal:
```shell
docker run -it ubuntu
```
4. Then enter the commands given by the instructions

When you want to exit simply type exit and it will return you to the command line for your actual computer
```shell
exit
```
<img src="https://emmanuelchristianos.github.io//assets/images/networking/ubuntuexit.png">

We can verify that we have exited the Linux container by looking at the prompt. A prompt in your terminal usually holds information regarding the computer you are on. Information like the current user that is logged on etc. My actual computer prompt you can see from before we ran any of the docker commands. Once we ran the docker container a different looking prompt appeared as we were then inside the Linux container; we had a Ubuntu prompt. After we exited the prompt returned to normal. The prompt is the easiest and quickest way to determine if you are still running inside your container or not.

<img src="https://emmanuelchristianos.github.io//assets/images/networking/blurredprompt.png">

You have now created an Ubuntu container using Docker.

For Windows Users docker requires some extra steps: follow along here [Docker for Windows](https://docs.docker.com/docker-for-windows/){: .fs-4 .mb-4 .mb-md-0 } or follow the VirtualBox installation of Ubuntu here [VirtualBox](#virtualbox-installation-and-setup){:.fs-4 .md-0 .mr-0 } which may be easier.

{: .d-inline}
</div>

#### VirtualBox Installation and Setup
{: .fs-5 .fw-200 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-2}

1. Go to [Virtual Box Downloads](https://www.virtualbox.org/wiki/Downloads){: .fs-4 .md-0 .mr-0 } click on the platform package that corresponds with your operating system and download VirtualBox
<img src="https://emmanuelchristianos.github.io//assets/images/networking/virtualboxdownload.png">
2. Next head to [Ubuntu Downloads](https://ubuntu.com/download/desktop){:.fs-4 .md-0 .mr-0 } And click download
<img src="https://emmanuelchristianos.github.io//assets/images/networking/ubuntudownload.png">
3. Open up virtual box
<details>
<summary> Warning: Unidentified Developer Solution [click]</summary>

<p id="warningP">
Some Mac users might receive a warning saying 'VirtualBox' can't be opened because it is from  an unidentified developer. If this happens to you follow these steps:
</p>

<p id="warningP">
1. Open up 'Systems Preferences'
</p>

<p id="warningP">
2. Navigate to 'Security & Privacy'
</p>

<p id="warningP">
3. On the menu tab at the top of the system preferences screen click the 'General' tab
</p>

<p id="warningP">
4. At the bottom of the 'General' tab you should see the unidentified developer warning for Virtual Box with a button next to it that says 'Open Anyway', click 'Open Anyway'
</p>
</details>
{: .d-block}


### Application Installation
{: .fs-6 .fw-400 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-1}

Coming
{: .d-block}
</div>


<div  markdown="1">
## Prerequisite Knowledge
{: .fs-7.fw-400 .d-inline-block}

Prerequisite
{: .fs-2 .fw-200 .label .label-purple .px-1 .py-0 .d-inline-block .mt-0}

Coming
{: .d-block}
</div>


<div  markdown="1">
## Core Knowledge
{: .fs-7.fw-400 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-0}

Coming
{: .d-block}

### What Is The Internet? An Introduction!
{: .fs-6 .fw-400 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-1}

Coming
{: .d-block}

#### How Is The Internet Composed?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### What Are Protocols?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### What Is Connecting To The Internet?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### What Devices Facilitate The Functionality Of The Internet?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### There Are Different Types Of Networks?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### Why Is Your Internet Slow Sometimes? How Delay Occurs!
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### What Is A Layered Protocol Stack?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

</div>

<div  markdown="1">
## Next Step
{: .fs-7.fw-400 .d-inline-block}

Next
{: .fs-2 .fw-200 .label .label-red .px-1 .py-0 .d-inline-block .mt-0}

Coming
{: .d-block}

### Practice This Knowledge
{: .fs-6 .fw-400 .d-inline-block}

Next
{: .fs-2 .fw-200 .label .label-red .px-1 .py-0 .d-inline-block .mt-1}

Coming
{: .d-block}

### What To Study Next?
{: .fs-6 .fw-400 .d-inline-block}

Next
{: .fs-2 .fw-200 .label .label-red .px-1 .py-0 .d-inline-block .mt-1}

Coming
{: .d-block}

</div>
