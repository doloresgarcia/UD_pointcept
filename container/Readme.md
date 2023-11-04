For building and for pulling the container,depending on your storage space, 
you main need to set APPTAINER_CACHEDIR and/or APPTAINER_TMPDIR to point to 
areas away from the default to avoid filling up /tmp and your home dir

Instructions to run the current container:
```bash
apptainer pull docker://kdlong/pointcept_cmspepr:v2
apptainer run -B /mnt/proj3 -B "/mnt/proj3/dd-23-142/Pointcept/data/PROCESSED_S3DIS/:/opt/pointcept/Pointcept/data" -B "/mnt/proj3/dd-23-142/Pointcept/exp/:/opt/pointcept/Pointcept/exp" --nv pointcept_pepr_v2.sif
```
The bind mounts are to enable you to run from /opt/pointcept and write to the project /mnt directory (/opt in the container is not writeable by default)

To build the container, run from a machine with sufficient memory. GPU is not required for build

From the folder containing Dockerfile
```bash
docker buildx build -t <dockerhub_username>/pointcept_cmspepr:v<version> .
docker push <dockerhub_username>/pointcept_cmspepr:v<version> .
```

You can see the list of images with ```docker images``` and you can rename with ```docker tag <imageid> <newname>```
