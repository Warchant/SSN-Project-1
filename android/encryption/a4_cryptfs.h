// https://android.googlesource.com/platform/system/vold/

#define CRYPT_MNT_MAGIC 0xD0B5B1C4
#define __le32 unsigned int
#define __le16 unsigned short int 
struct crypt_mnt_ftr {
  __le32 magic;		/* See above */
  __le16 major_version;
  __le16 minor_version;
  __le32 ftr_size; 	/* in bytes, not including key following */
  __le32 flags;		/* See above */
  __le32 keysize;	/* in bytes */
  __le32 spare1;	/* ignored */
  __le64 fs_size;	/* Size of the encrypted fs, in 512 byte sectors */
  __le32 failed_decrypt_count; /* count of # of failed attempts to decrypt and
				  mount, set to 0 on successful mount */
  unsigned char crypto_type_name[MAX_CRYPTO_TYPE_NAME_LEN]; /* The type of encryption
							       needed to decrypt this
							       partition, null terminated */
};
