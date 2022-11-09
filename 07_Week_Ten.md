# Code Toolkit: Python, Fall 2021

# Week 10 — Wednesday, November 2 — Class notes

# Command line from [Sam](https://github.com/antiboredom/scrapism-fall-2022/blob/main/01-command-line/01-notes.md)

    # The Command Line

The command line is a text-based interface for interacting with your computer. From the command line you can launch programs, view files, and manipulate your file system by making, moving, and copying files and directories. You can think of it as the Finder in Mac, without the graphic interface, but much more powerful.

## Setup


On a Mac you can access the command line by opening up the `Terminal` application, located in `/Applications/Utilities/Terminal`

To get started on Windows you will need to set up the Windows Subsystem for Linux, which allows you to run Ubuntu (a Linux distribution) from within your current Windows 10 installation.  [Follow this guide to do so](https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows). Alternatively, you can install [Git for Windows](https://gitforwindows.org/) which includes many of the commands I'll be covering below.


---


## The Prompt

When you open up your terminal application you'll see something like this:

```bash
sam@SamsComputer ~ % 
```

This is called the "prompt". By default (on a Mac) it shows your username, an `@` symbol, the name of your computer, the directory that you are currently in, and then a `%` sign.

The basic use of the command line is: 1) you type a command, 2) you hit return, and 3) some output of the command is printed to the screen.

Whatever you type will start appearing after the end of the prompt line.

---

## Basic Navigation & File Operations

*Please note I use the word "directory" and "folder" interchangeably.*

When you open a new terminal window, you are placed inside your home folder. On a Mac this is `/Users/myusername` and on Linux, `/home/myusername`.

To see the folder you are currently in, type: `pwd` and hit return. `pwd` stands for "print working directory", or in other words, "show me the directory I am currently working from".

### Getting around, making, deleting and copying files and folders.


**`pwd`** stands for "print working directory". It prints out where you are:

```bash
pwd
```

**`ls`** stands for "list". It lists the contents of current directory.

```bash
ls
```

**`cd`** stands for "change directory". Type `cd` and then the directory you want to go to. For example, change to the Desktop from your home folder:

```bash
cd Desktop
```

To go into the parent folder, up one level in the file structure, type `..` or `../` instead of a folder name, like so:

```bash
cd ..
```

If you type `cd` without a folder name after, it takes you back to your home folder.


**`mkdir`** stands for "make directory". Type `mkdir` and then a name to make a folder. For example, make a folder called "cool_project":

```bash
mkdir cool_project
```

**`mv`** stands for "move". It lets you move files and folders and also rename them. To rename a file:

```bash
mv oldname.txt newname.txt
```

**`cp`** stands for "copy". It lets you duplicate files:

```bash
cp draft.txt draft_copy.txt
```

**`rm`** stands for "remove". It lets you delete files:

```bash
rm bad_selfie.jpg
```

Please note, `rm` will **not** ask for confirmation, and it will not move files to the trash. It'll just delete them immediately, so be careful.


**`file`** provides basic info about a file:

```bash
file mysterfile.what
```

## The Structure of the Filesystem

Everything on your computer is either a file or a folder, and these files and folders are organized hierarchically, like a tree. At the very bottom of the tree is the "root folder", indicated by a single forward slash, like so `/`. Here's a basic example of directory structure:

```bash
/
	Users/
  		sam/
   			Desktop/
	  			trotsky.jpg
	  			the_man_without_qualities.txt
	 		Documents/
	 		Downloads/
		Guest/
	Applications/
	Volumes/
```

Each file and folder has a unique location on the filesystem. This location is called a "path". You can reference files and folders either by their **relative** path, or by their **absolute** or **full** path. In the previous examples I have been using the relative path - that is, I have been referencing files relative to where I currently am. **A path is absolute if it begins with a `/`**

For example the absolute path to `the_man_without_qualities.txt` in the above filesystem is `/Users/sam/Desktop/the_man_without_qualities.txt`. I can look inside the contents of this file, from any working directory, with this command:

```bash
more /Users/sam/Desktop/the_man_without_qualities.txt
```

There are a few shortcuts for dealing paths as well.

`.` (single dot) or `'./'` (single dot with slash) means the current folder that I am in.

`..` (two dots) or `../` (two dots with slash) means the parent folder. For example, if am in my Desktop folder and I want to list the contents of my Downloads folder I could type:

```bash
ls ../Downloads/
```

Finally, the `~` symbol refers to your home folder.

---

## Tips

It can take a while to get used to the command line, but there are a few tips and trick that make it much easier to use.

* Use the up and down arrows to view a history of the commands you have entered.
* Hit the tab key to autocomplete commands and file paths
* Type `open` and then a filename to open the file in its default program
* Type `open .` to open the current folder in the Finder
* Drag a folder or file onto the terminal to fill in its absolute path
* Type `ctrl-a` to move your cursor to the beginning of the line, and `ctrl-e` to the end

---

## Reading and manipulating text files (basics)

**`cat`** stands for "concatenate" and it shows you the contents of a file and also allows you to join two files together. For example, to print out the entirety of the Communist Manifesto:

```bash
cat manifesto.txt
```

**`more`** is like `cat` but will paginate the output if it is larger than the size of your terminal window:

```bash
more manifesto.txt
```
(now use the up and down arrows to go up or down by a line, the space to go down by a page and `q` to exit if needed)


**`sort`** sorts a file alphabetically by line and prints the output to the screen

```bash
sort names.txt
```

**`grep`** searches each line of a file for some input, and prints those lines to the screen. For example, the following searches for all lines in the Communist Manifesto containing the word "Communist".

```bash
grep Communist manifesto.txt
```
---


## Command Line Options and Getting Help

Most commands have extra options that you can input when you run the command.  They are usually preceded by either one or two dashes (`-` or `--`).

The structure of a typical command looks like this:

```bash
command_name [options] arguments
```

("arguments" refers to the file or files your are running the command with)

For example, the `sort` command outputs in ascending order by default, but you can have it use reverse order with the `-r` option, like so:

```bash
sort -r manifesto.txt
```

You can also tell `sort` to only output unique lines (ie, to remove any duplicate lines) with the `-u` option:

```bash
sort -u manifesto.txt
```

Finally you can combine options:

```bash
sort -u -r manifesto.txt
```

Another fun example is the `say` command, which outputs text as computer speech.

```bash
say "a specter is haunting this computer"
```

Sometimes options have parameters. For example, the `say` command allows you to change its voice with the `-v` option, followed by the name of a computer voice.


```bash
say -v Amelie "the specter of communism"
```

You can change the rate at which words are spoken using `-r NUM` where `NUM` is a number.


```bash
say -v Amelie "the specter of communism" -r 100
```

To see all the options and view a manual for any command, use the `man` tool (short for "manual")

```bash
man say
```

When viewing a manual page, use the arrow keys to navigate, and `q` to exit.

And of course, if you can't remember a command or option, just google it! Sometimes it's much easier than searching through the man pages...

---

## Piping and Directing Output

Most commands will produce output on the screen. However we can also automatically save that output to the file system using the `>` character followed by a filename.

Sort a file called "names.txt", and save the output to a new file called "sorted_names.txt":

```bash
sort names.txt > sorted_names.txt
```

`>` will create a file if it does not already exist, or overwrite one if it does. You can use `>>` instead to append to a file.

Unix also has a very powerful concept called "pipes" which allow us to chain commands together, effectively feeding the output of one command into the input of another. To do so, we use the `|` symbol.

Extract all lines of the Communist Manifesto containing "Communist", then sort them.

```bash
grep Communist manifesto.txt | sort -u
```

The `|` here means "take the output of the grep command and send it to sort -u". You can use as many pipes as you desire, and combine this technique with the output redirection.

Extract all lines of the Communist Manifesto containing "Communist", then sort them, then save to a new file called "sorted_communists.txt"

```bash
grep Communist manifesto.txt | sort -u > sorted_communists.txt
```

---

## Intermediate text manipulation

Here are a few slightly more advanced techniques for manipulating text on the command line.

### Breaking lines into words or other segments

**`cut`** cuts out a portion of each line and splits it out according to a delimiter. If you use a space `" "` as a delimiter, it breaks a line up into words:

```bash
cut -d " " manifesto.txt
```

The `-f` option allows you to specify a particular item to grab. `-f 1` grabs just the first word.

```bash
cut -d " " -f 1 manifesto.txt
```

Try combining this with other commands, like `sort` or `grep`.

```bash
cut -d " " -f 2 manifesto.txt | sort -u -R
```

### Finding and replacing

**`sed`** is a somewhat complex tool that allows you to find and replace things in text files. It takes an argument with a command using it's own special syntax, like so `s/FIND/REPLACE/g`.

For example, replace all instances of "you" with "me":

```bash
sed 's/you/me/g' sometext.txt
```

By default, `sed` is case sensitive. To make it case insensitive, add an `i` at the end:

```bash
sed 's/you/me/gi' sometext.txt
```

Sometimes, I'll just find something online that seems useful without really understanding how it works. You should definitely give this a shot. For example, here's how you use `sed` to split a text into sentences: 

```bash
sed 's/[.!?]  */&\n/g' manifesto.txt
```

You can do a ton of other stuff with `sed`. If you want to learn more, take a look at this [tutorial](https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux)


---

## Downloading stuff

There are two very useful commands for downloading stuff from the internet.


### cURL

**`curl`** makes a http request, and prints the output to the terminal. For example, this grabs the html source of NPR's text only news page:

```bash
curl https://text.npr.org
```

This is a bit hard to read because it's full of html. But there are a bunch of little websites that are specifically designed to be "curled".

To get the weather:

```bash
curl wttr.in
```

Stats about covid:

```bash
curl https://corona-stats.online
```

Generate QR codes:

```bash
curl "qrenco.de/but why"
```

Many more [here](https://github.com/chubin/awesome-console-services)!

### wget

**`wget`** allows you to easily download files:

```bash
wget "https://www.gutenberg.org/cache/epub/61/pg61.txt"
```

You can also specify a name to save the file as with the `-O` option.

```bash
wget "https://www.gutenberg.org/cache/epub/61/pg61.txt" -O manifesto.txt
```

---

## Aliases

(to come)


## Scripts

(to come)


## Wildcards

It's possible to reference multiple files using the `*` character in combination with other characters. This can be really useful in a lot of situations.

For example, can list all files that begin with the word "the" like so:

```bash
ls the*
```

List all jpg images:

```bash
ls *.jpg
```

Make a folder called `images` and move all jpeg images into it:

```bash
mkdir images
mv *.jpg images/
```

Combine all text files in a folder:

```
cat *.txt > everything.txt
```
]

# Stable Diffusion
## **macOS Instructions**

Requirements

- macOS 12.3 Monterey or later
- Python
- Patience
- Apple Silicon\*

\*I haven't tested any of this on Intel Macs but I have read that one person got it to work, so Apple Silicon might not be requried.

Things have moved really fast and so these instructions change often
and are often out-of-date. One of the problems is that there are so
many different ways to run this.

We are trying to build a testing setup so that when we make changes it
doesn't always break.

How to (this hasn't been 100% tested yet):

First get the weights checkpoint download started - it's big:

1. Sign up at https://huggingface.co
2. Go to the [Stable diffusion diffusion model page](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original)
3. Accept the terms and click Access Repository:
4. Download [sd-v1-4.ckpt (4.27 GB)](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/blob/main/sd-v1-4.ckpt) and note where you have saved it (probably the Downloads folder)

While that is downloading, open Terminal and run the following commands one at a time.

```bash
# install brew (and Xcode command line tools):
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

#
# Now there are two different routes to get the Python (miniconda) environment up and running:
# 1. Alongside pyenv
# 2. No pyenv
#
# If you don't know what we are talking about, choose 2.
#
# NOW EITHER DO
# 1. Installing alongside pyenv

brew install pyenv-virtualenv # you might have this from before, 
brew install cmake protobuf rust
# no problem
pyenv install anaconda3-2022.05
pyenv virtualenv anaconda3-2022.05
eval "$(pyenv init -)"
pyenv activate anaconda3-2022.05

# OR,
# 2. Installing standalone
# install python 3, git, cmake, protobuf:
brew install cmake protobuf rust

# install miniconda (M1 arm64 version):
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o Miniconda3-latest-MacOSX-arm64.sh
/bin/bash Miniconda3-latest-MacOSX-arm64.sh


# EITHER WAY,
# continue from here

# clone the repo
git clone https://github.com/lstein/stable-diffusion.git
cd stable-diffusion

#
# wait until the checkpoint file has downloaded, then proceed
#

# create symlink to checkpoint
mkdir -p models/ldm/stable-diffusion-v1/

PATH_TO_CKPT="$HOME/Downloads"  # or wherever you saved sd-v1-4.ckpt

ln -s "$PATH_TO_CKPT/sd-v1-4.ckpt" models/ldm/stable-diffusion-v1/model.ckpt

# install packages
PIP_EXISTS_ACTION=w CONDA_SUBDIR=osx-arm64 conda env create -f environment-mac.yaml
conda activate ldm

# only need to do this once
python scripts/preload_models.py

# run SD!
python scripts/dream.py --full_precision  # half-precision requires autocast and won't work
```

The original scripts should work as well.

```
python scripts/orig_scripts/txt2img.py --prompt "a photograph of an astronaut riding a horse" --plms
```

Note, `export PIP_EXISTS_ACTION=w` is a precaution to fix `conda env
create -f environment-mac.yaml` never finishing in some situations. So
it isn't required but wont hurt.

After you follow all the instructions and run dream.py you might get several errors. Here's the errors I've seen and found solutions for.

### Is it slow?

Be sure to specify 1 sample and 1 iteration.

    python ./scripts/orig_scripts/txt2img.py --prompt "ocean" --ddim_steps 5 --n_samples 1 --n_iter 1

### Doesn't work anymore?

PyTorch nightly includes support for MPS. Because of this, this setup is inherently unstable. One morning I woke up and it no longer worked no matter what I did until I switched to miniforge. However, I have another Mac that works just fine with Anaconda. If you can't get it to work, please search a little first because many of the errors will get posted and solved. If you can't find a solution please [create an issue](https://github.com/lstein/stable-diffusion/issues).

One debugging step is to update to the latest version of PyTorch nightly.

    conda install pytorch torchvision torchaudio -c pytorch-nightly

If `conda env create -f environment-mac.yaml` takes forever run this.

    git clean -f

And run this.

    conda clean --yes --all

Or you could reset Anaconda.

    conda update --force-reinstall -y -n base -c defaults conda

### "No module named cv2", torch, 'ldm', 'transformers', 'taming', etc.

There are several causes of these errors.

First, did you remember to `conda activate ldm`? If your terminal prompt
begins with "(ldm)" then you activated it. If it begins with "(base)"
or something else you haven't.

Second, you might've run `./scripts/preload_models.py` or `./scripts/dream.py`
instead of `python ./scripts/preload_models.py` or `python ./scripts/dream.py`.
The cause of this error is long so it's below.

Third, if it says you're missing taming you need to rebuild your virtual
environment.

    conda env remove -n ldm
    conda env create -f environment-mac.yaml

Fourth, If you have activated the ldm virtual environment and tried rebuilding it, maybe the problem could be that I have something installed that you don't and you'll just need to manually install it. Make sure you activate the virtual environment so it installs there instead of
globally.

    conda activate ldm
    pip install *name*

You might also need to install Rust (I mention this again below).

### How many snakes are living in your computer?

You might have multiple Python installations on your system, in which case it's
important to be explicit and consistent about which one to use for a given project.
This is because virtual environments are coupled to the Python that created it (and all
the associated 'system-level' modules).

When you run `python` or `python3`, your shell searches the colon-delimited locations
in the `PATH` environment variable (`echo $PATH` to see that list) in that order - first match wins.
You can ask for the location of the first `python3` found in your `PATH` with the `which` command like this:

    % which python3
    /usr/bin/python3

Anything in `/usr/bin` is [part of the OS](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html#//apple_ref/doc/uid/TP40010672-CH2-SW6). However, `/usr/bin/python3` is not actually python3, but 
rather a stub that offers to install Xcode (which includes python 3). If you have Xcode installed already,
`/usr/bin/python3` will execute `/Library/Developer/CommandLineTools/usr/bin/python3` or
`/Applications/Xcode.app/Contents/Developer/usr/bin/python3` (depending on which
Xcode you've selected with `xcode-select`).

Note that `/usr/bin/python` is an entirely different python - specifically, python 2. Note: starting in
macOS 12.3, `/usr/bin/python` no longer exists.

    % which python3
    /opt/homebrew/bin/python3

If you installed python3 with Homebrew and you've modified your path to search
for Homebrew binaries before system ones, you'll see the above path.

    % which python
    /opt/anaconda3/bin/python

If you have Anaconda installed, you will see the above path. There is a
`/opt/anaconda3/bin/python3` also. We expect that `/opt/anaconda3/bin/python` 
and `/opt/anaconda3/bin/python3` should actually be the *same python*, which you can
verify by comparing the output of `python3 -V` and `python -V`.

    (ldm) % which python
    /Users/name/miniforge3/envs/ldm/bin/python

The above is what you'll see if you have miniforge and you've correctly activated
the ldm environment, and you used option 2 in the setup instructions above ("no pyenv").

    (anaconda3-2022.05) % which python
    /Users/name/.pyenv/shims/python
    
... and the above is what you'll see if you used option 1 ("Alongside pyenv").

It's all a mess and you should know [how to modify the path environment variable](https://support.apple.com/guide/terminal/use-environment-variables-apd382cc5fa-4f58-4449-b20a-41c53c006f8f/mac)
if you want to fix it. Here's a brief hint of all the ways you can modify it
(don't really have the time to explain it all here).

- ~/.zshrc
- ~/.bash_profile
- ~/.bashrc
- /etc/paths.d
- /etc/path

Which one you use will depend on what you have installed except putting a file
in /etc/paths.d is what I prefer to do.

Finally, to answer the question posed by this section's title, it may help to list 
all of the `python` / `python3` things found in `$PATH` instead of just the one that
will be executed by default. To do that, add the `-a` switch to `which`:

    % which -a python3
    ...

### Debugging?

Tired of waiting for your renders to finish before you can see if it
works? Reduce the steps! The image quality will be horrible but at least you'll
get quick feedback.

    python ./scripts/txt2img.py --prompt "ocean" --ddim_steps 5 --n_samples 1 --n_iter 1

### OSError: Can't load tokenizer for 'openai/clip-vit-large-patch14'...

    python scripts/preload_models.py

### "The operator [name] is not current implemented for the MPS device." (sic)

Example error.

```
...
NotImplementedError: The operator 'aten::_index_put_impl_' is not current implemented for the MPS device. If you want this op to be added in priority during the prototype phase of this feature, please comment on [https://github.com/pytorch/pytorch/issues/77764](https://github.com/pytorch/pytorch/issues/77764). As a temporary fix, you can set the environment variable `PYTORCH_ENABLE_MPS_FALLBACK=1` to use the CPU as a fallback for this op. WARNING: this will be slower than running natively on MPS.
```

The lstein branch includes this fix in [environment-mac.yaml](https://github.com/lstein/stable-diffusion/blob/main/environment-mac.yaml).

### "Could not build wheels for tokenizers"

I have not seen this error because I had Rust installed on my computer before I started playing with Stable Diffusion. The fix is to install Rust.

    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

### How come `--seed` doesn't work?

First this:

> Completely reproducible results are not guaranteed across PyTorch
> releases, individual commits, or different platforms. Furthermore,
> results may not be reproducible between CPU and GPU executions, even
> when using identical seeds.

[PyTorch docs](https://pytorch.org/docs/stable/notes/randomness.html)

Second, we might have a fix that at least gets a consistent seed sort of. We're
still working on it.

### libiomp5.dylib error?

    OMP: Error #15: Initializing libiomp5.dylib, but found libomp.dylib already initialized.

You are likely using an Intel package by mistake. Be sure to run conda with
the environment variable `CONDA_SUBDIR=osx-arm64`, like so:

`CONDA_SUBDIR=osx-arm64 conda install ...`

This error happens with Anaconda on Macs when the Intel-only `mkl` is pulled in by
a dependency. [nomkl](https://stackoverflow.com/questions/66224879/what-is-the-nomkl-python-package-used-for)
is a metapackage designed to prevent this, by making it impossible to install
`mkl`, but if your environment is already broken it may not work.

Do _not_ use `os.environ['KMP_DUPLICATE_LIB_OK']='True'` or equivalents as this
masks the underlying issue of using Intel packages.

### Not enough memory.

This seems to be a common problem and is probably the underlying
problem for a lot of symptoms (listed below). The fix is to lower your
image size or to add `model.half()` right after the model is loaded. I
should probably test it out. I've read that the reason this fixes
problems is because it converts the model from 32-bit to 16-bit and
that leaves more RAM for other things. I have no idea how that would
affect the quality of the images though.

See [this issue](https://github.com/CompVis/stable-diffusion/issues/71).

### "Error: product of dimension sizes > 2\*\*31'"

This error happens with img2img, which I haven't played with too much
yet. But I know it's because your image is too big or the resolution
isn't a multiple of 32x32. Because the stable-diffusion model was
trained on images that were 512 x 512, it's always best to use that
output size (which is the default). However, if you're using that size
and you get the above error, try 256 x 256 or 512 x 256 or something
as the source image.

BTW, 2\*\*31-1 = [2,147,483,647](https://en.wikipedia.org/wiki/2,147,483,647#In_computing), which is also 32-bit signed [LONG_MAX](https://en.wikipedia.org/wiki/C_data_types) in C.

### I just got Rickrolled! Do I have a virus?

You don't have a virus. It's part of the project. Here's
[Rick](https://github.com/lstein/stable-diffusion/blob/main/assets/rick.jpeg)
and here's [the
code](https://github.com/lstein/stable-diffusion/blob/69ae4b35e0a0f6ee1af8bb9a5d0016ccb27e36dc/scripts/txt2img.py#L79)
that swaps him in. It's a NSFW filter, which IMO, doesn't work very
good (and we call this "computer vision", sheesh).

Actually, this could be happening because there's not enough RAM. You could try the `model.half()` suggestion or specify smaller output images.

### My images come out black

We might have this fixed, we are still testing.

There's a [similar issue](https://github.com/CompVis/stable-diffusion/issues/69)
on CUDA GPU's where the images come out green. Maybe it's the same issue?
Someone in that issue says to use "--precision full", but this fork
actually disables that flag. I don't know why, someone else provided
that code and I don't know what it does. Maybe the `model.half()`
suggestion above would fix this issue too. I should probably test it.

### "view size is not compatible with input tensor's size and stride"

```
  File "/opt/anaconda3/envs/ldm/lib/python3.10/site-packages/torch/nn/functional.py", line 2511, in layer_norm
    return torch.layer_norm(input, normalized_shape, weight, bias, eps, torch.backends.cudnn.enabled)
RuntimeError: view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.
```

Update to the latest version of lstein/stable-diffusion. We were
patching pytorch but we found a file in stable-diffusion that we could
change instead. This is a 32-bit vs 16-bit problem.

### The processor must support the Intel bla bla bla

What? Intel? On an Apple Silicon?

    Intel MKL FATAL ERROR: This system does not meet the minimum requirements for use of the Intel(R) Math Kernel Library.
    The processor must support the Intel(R) Supplemental Streaming SIMD Extensions 3 (Intel(R) SSSE3) instructions.
    The processor must support the Intel(R) Streaming SIMD Extensions 4.2 (Intel(R) SSE4.2) instructions.
    The processor must support the Intel(R) Advanced Vector Extensions (Intel(R) AVX) instructions.

This is due to the Intel `mkl` package getting picked up when you try to install
something that depends on it-- Rosetta can translate some Intel instructions but
not the specialized ones here. To avoid this, make sure to use the environment
variable `CONDA_SUBDIR=osx-arm64`, which restricts the Conda environment to only
use ARM packages, and use `nomkl` as described above.

### input types 'tensor<2x1280xf32>' and 'tensor<\*xf16>' are not broadcast compatible

May appear when just starting to generate, e.g.:

```
dream> clouds
Generating:   0%|                                                              | 0/1 [00:00<?, ?it/s]/Users/[...]/dev/stable-diffusion/ldm/modules/embedding_manager.py:152: UserWarning: The operator 'aten::nonzero' is not currently supported on the MPS backend and will fall back to run on the CPU. This may have performance implications. (Triggered internally at /Users/runner/work/_temp/anaconda/conda-bld/pytorch_1662016319283/work/aten/src/ATen/mps/MPSFallback.mm:11.)
  placeholder_idx = torch.where(
                                                                                                    loc("mps_add"("(mpsFileLoc): /AppleInternal/Library/BuildRoots/20d6c351-ee94-11ec-bcaf-7247572f23b4/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Core/Files/MPSGraphUtilities.mm":219:0)): error: input types 'tensor<2x1280xf32>' and 'tensor<*xf16>' are not broadcast compatible
LLVM ERROR: Failed to infer result type(s).
Abort trap: 6
/Users/[...]/opt/anaconda3/envs/ldm/lib/python3.9/multiprocessing/resource_tracker.py:216: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```

Macs do not support autocast/mixed-precision. Supply `--full_precision` to use float32 everywhere.


```
eval "$(pyenv init -)"
pyenv activate anaconda3-2022.05
conda activate invokeai
python scripts/dream.py --full_precision 
```
